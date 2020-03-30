package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
	"time"

	"github.com/dghubble/go-twitter/twitter"
	"github.com/dghubble/oauth1"
)

type Credentials struct {
	ConsumerKey       string
	ConsumerSecret    string
	AccessToken       string
	AccessTokenSecret string
}

// Simple linkedlist implementation adapted from https://gist.github.com/bemasher/1777766
type Stack struct {
	top  *Element
	size int
}

type Element struct {
	book   string
	source string
	verse  string
	next   *Element
}

func (s *Stack) Size() int {
	return s.size
}

func (s *Stack) Push(book string, source string, verse string) {
	s.top = &Element{book, source, verse, s.top}
	s.size++
}

func (s *Stack) Pop() (verse string, source string) {
	if s.size > 0 {
		verse, source, s.top = s.top.verse, s.top.book+" "+s.top.source, s.top.next
		s.size--
		return
	}
	return "", ""
}

const ThirtyMinute = 1800

func main() {
	llverse := loadVerse()
	tweetCount := 0

	creds := Credentials{
		AccessToken:       os.Getenv("ACCESS_TOKEN"),
		AccessTokenSecret: os.Getenv("ACCESS_TOKEN_SECRET"),
		ConsumerKey:       os.Getenv("CONSUMER_KEY"),
		ConsumerSecret:    os.Getenv("CONSUMER_SECRET"),
	}

	client, err := getClient(&creds)
	if err != nil {
		log.Println("Twitter Client Error")
		log.Println(err)
	}

	for {
		current := time.Now().Unix()

		if current%ThirtyMinute == 0 {
			verse, source := llverse.Pop()
			tweet := verse + source
			client.Statuses.Update(tweet, nil)
			tweetCount += 1
			fmt.Println("Created tweet #", tweetCount)
			if llverse.Size() == 0 {
				llverse = loadVerse()
			}

			time.Sleep(29 * time.Minute)
		}
	}

}

func loadVerse() *Stack {
	// owoBible text adapted and modified with the help of Luis Hoderlein https://github.com/khemritolya
	file, err := os.Open("owoBible.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	llverse := new(Stack)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		book := line[:strings.Index(line, "||")]
		chapter := line[len(book)+2 : strings.LastIndex(line, "||")]
		verse := line[strings.LastIndex(line, "||")+2:]
		llverse.Push(book, chapter, verse)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return llverse
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
