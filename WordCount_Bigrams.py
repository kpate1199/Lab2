import sys
import re

def map_function(input):
    try:
        words = re.findall(r"[\w']+", input)
        for i in range(len(words) - 1):
            bigram = f'"{words[i]},{words[i+1]}"'
            print(f"{bigram} 1")
    except Exception as e:
        print(f"Error in map_function: {str(e)}")

def reduce_function():
    try:
        bigram_counts = {}
        for line in sys.stdin:
            try:
                bigram, count = line.strip().split()
                count = int(count)

                # Aggregate bigram counts
                bigram_counts[bigram] = bigram_counts.get(bigram, 0) + count
            except ValueError:
                print(f"Unable to split the line into bigram and count - {line}")

        # Print bigram counts
        for bigram, count in bigram_counts.items():
            print(f'{bigram} {count}')
    except Exception as e:
        print(f"Error in reduce_function: {str(e)}")

if __name__ == "__main__":
    try:
        
        for line in sys.stdin:
            
            map_function(line)

        
        reduce_function()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
