package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os/exec"
	"strings"
	"log"
	"os"
	"github.com/dghubble/go-twitter/twitter"
    "github.com/dghubble/oauth1"
)

type Credentials struct {
    ConsumerKey       string
    ConsumerSecret    string
    AccessToken       string
    AccessTokenSecret string
}

func main() {


	creds := Credentials{
		AccessToken:       os.Getenv("ACCESS_TOKEN"),
		AccessTokenSecret: os.Getenv("ACCESS_TOKEN_SECRET"),
		ConsumerKey:       os.Getenv("CONSUMER_KEY"),
		ConsumerSecret:    os.Getenv("CONSUMER_SECRET"),
	}

	client, err := getClient(&creds)
	if err != nil {
		log.Println("Error getting Twitter Client")
		log.Println(err)
	}

	
	verse, source := GetVerse()
	tweet := verse + source

	client.Statuses.Update(tweet, nil)


}

func GetVerse() (string, string){
	bibleURL := "https://beta.ourmanna.com/api/v1/get/?format=text&order=random"

	bibleRequest, err := http.NewRequest("GET", bibleURL, nil)
	if err != nil {
		log.Fatal(err)
	}

	bibleResponse, err := http.DefaultClient.Do(bibleRequest)
	if err != nil {
		log.Fatal(err)
	}

	defer bibleResponse.Body.Close()
	output, _ := ioutil.ReadAll(bibleResponse.Body)

	verse := strings.TrimSpace(string(output))

	cutOff := strings.Index(verse, " - ")
	actualVerse := strings.TrimSpace(string(verse[:cutOff]))
	source := strings.TrimSpace(string(verse[cutOff:]))

	pythonPassthrough := "import owo; print(owo.owo(\"\"\"" + actualVerse + "\"\"\"))"

	cmd := exec.Command("python",  "-c", pythonPassthrough)

	out, _ := cmd.CombinedOutput()

	return string(out), source
}


// https://tutorialedge.net/golang/writing-a-twitter-bot-golang/
func getClient(creds *Credentials) (*twitter.Client, error) {

    config := oauth1.NewConfig(creds.ConsumerKey, creds.ConsumerSecret)

    token := oauth1.NewToken(creds.AccessToken, creds.AccessTokenSecret)

    httpClient := config.Client(oauth1.NoContext, token)
    client := twitter.NewClient(httpClient)

    verifyParams := &twitter.AccountVerifyParams{
        SkipStatus:   twitter.Bool(true),
        IncludeEmail: twitter.Bool(true),
    }

    user, _, err := client.Accounts.VerifyCredentials(verifyParams)
    if err != nil {
        return nil, err
    }

    log.Printf("User's ACCOUNT:\n%+v\n", user)
    return client, nil
}
