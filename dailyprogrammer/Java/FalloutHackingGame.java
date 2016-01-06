/*
    reddit.com/r/dailyprogrammer
    Challenge #238 Intermediate
    Fallout Hacking Game
	https://redd.it/3qjnil

    Solution by whoisrgj.
    http://www.whoisrgj.com
 */
 
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class FalloutHackingGame {

    final static int DEFAULT_GUESSES_ALLOWED = 4;

    private boolean isRunning;
    private int wordLength;
    private int wordCount;
    private int guessesLeft;
    private Random randomGenerator;
    private String answer;
    private List<String> randomWordList;

    public FalloutHackingGame() {
        this(DEFAULT_GUESSES_ALLOWED);
    }

    public FalloutHackingGame(int guessesAllowed) {
        setGuessesLeft(guessesAllowed);
    }

    public void startGame() {
        // initialize random generator and scanner
        this.randomGenerator = new Random();
        Scanner scanner = new Scanner(System.in);

        // ask for difficulty level
        System.out.format("Difficulty (1-5)? ");
        setDifficultyLevel(scanner.nextInt());

        // generate randomWordList
        try {
            this.randomWordList = getRandomWordList();
        } catch (IOException e) {
            e.printStackTrace();
        }

        // randomly select the answer
        setAnswer(randomWordList.get(this.randomGenerator.nextInt(randomWordList.size())));

        // print the randomWordList
        for(int i = 0; i < wordCount; i++)
            System.out.format("%d) %s\n", i+1, randomWordList.get(i));

        setIsRunning(true);
        int userGuess, charactersCorrect;
        while(getIsRunning()) {
            System.out.format("Guess (%d left)? ", getGuessesLeft());
            userGuess = scanner.nextInt();
            if(userGuess < 1 || userGuess > wordCount) {
                System.out.format("You selection was out of range (1-%d). Try again.\n", wordCount);
                continue;
            }
            userGuess--;
            charactersCorrect = getCharactersCorrect(randomWordList.get(userGuess));
            setGuessesLeft(getGuessesLeft()-1);

            System.out.format("Your selection: %s\n", randomWordList.get(userGuess));
            System.out.format("%d/%d correct\n", charactersCorrect, wordLength);
            if(charactersCorrect == wordLength) {
                System.out.println("You win! Congrats.");
                setIsRunning(false);
            } else if(getGuessesLeft() < 1) {
                System.out.format("You lost! The answer was '%s'.\n", getAnswer());
                setIsRunning(false);
            }
        }
    }

    private int getCharactersCorrect(String word) {
        int correct = 0;
        for(int i = 0; i < wordLength; i++)
            if(getAnswer().charAt(i) == word.charAt(i))
                correct++;
        return correct;
    }

    private List<String> getRandomWordList() throws IOException {
        // read words from file
        FileReader fileReader = new FileReader("enable1.txt");
        BufferedReader bufferedReader = new BufferedReader(fileReader);

        // initialize an ArrayList for words of wordLength in file
        List<String> wordList = new ArrayList<String>();

        // add words of wordLength to wordList
        String word;
        while((word = bufferedReader.readLine()) != null)
            if(word.length() == this.wordLength)
                wordList.add(word);

        // create random word list
        List<String> randomWordList = new ArrayList<String>();
        for(int i = 0; i < this.wordCount; i++)
            randomWordList.add(wordList.get(this.randomGenerator.nextInt(wordList.size())));

        // return the random word list
        return randomWordList;
    }

    /*
        SETTERS
     */
    private void setIsRunning(boolean isRunning) {
        this.isRunning = isRunning;
    }

    private void setDifficultyLevel(int difficultyLevel) {
        switch(difficultyLevel) {
            case 1:
                this.wordCount = 5;
                this.wordLength = 4;
                break;
            case 2:
                this.wordCount = 7;
                this.wordLength = 7;
                break;
            case 4:
                this.wordCount = 13;
                this.wordLength = 12;
                break;
            case 5:
                this.wordCount = 15;
                this.wordLength = 15;
                break;
            default:
                this.wordCount = 10;
                this.wordLength = 10;
        }
    }

    private void setGuessesLeft(int guessesLeft) {
        this.guessesLeft = guessesLeft;
    }

    private void setAnswer(String answer) {
        this.answer = answer;
    }

    /*
        GETTERS
     */
    private boolean getIsRunning() {
        return this.isRunning;
    }

    private int getGuessesLeft() {
        return this.guessesLeft;
    }

    private String getAnswer() {
        return this.answer;
    }
}
