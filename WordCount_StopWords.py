import sys


stopWords = {"the", "and", "of", "a", "to", "in", "is", "it"}

def mapper(input):
    try:
        words = input.split()
        for word in words:
            
            if word.lower() not in stopWords:
                # Remove each non-stopword with a count of 1
                print(f"{word} 1")
    except Exception as e:
        print(f"Error in mapper: {str(e)}")

def reducer():
    try:
        word_counts = {}
        for line in sys.stdin:
            try:
                word, count = line.strip().split()
                count = int(count)

                # Aggregate word counts
                word_counts[word] = word_counts.get(word, 0) + count
            except ValueError:
                print(f"Unable to split the line into word and count - {line}")

        # Output the final word counts
        for word, count in word_counts.items():
            print(f'"{word}" {count}')
    except Exception as e:
        print(f"Error in reducer: {str(e)}")

if __name__ == "__main__":
    try:
        # Read input from standard input
        for line in sys.stdin:
            # Map step
            mapper(line)

        # Reduce step
        reducer()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
