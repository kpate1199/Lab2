import sys

def mapper(input):
    words = input.split()
    for word in words:
        # Remove each word with a count of 1
        print(f"{word} 1")

def reducer():
    word_counts = {}
    for line in sys.stdin:
        try:
            word, count = line.strip().split()
            count = int(count)

            # Aggregate word counts
            word_counts[word] = word_counts.get(word, 0) + count
        except ValueError:
            print(f"Unable to split the line into word and count - {line}")

    # Print word counts
    for word, count in word_counts.items():
        print(f'"{word}" {count}')

if __name__ == "__main__":
    try:
        example_input = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Donec condimentum elit vel mauris varius, id laoreet tortor placerat.
        Nulla scelerisque felis ac risus varius, sit sit amet luctus elit mattis."""

        
        mapper(example_input)

        
        reducer()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
