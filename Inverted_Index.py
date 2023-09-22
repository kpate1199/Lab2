import sys

def map_function(doc_no, text):
    try:
        words = text.split()
        for word in words:
            # Remove each word and the document it appears in
            print(f'"{word}" "{doc_no}"')
    except Exception as e:
        print(f"Error in map_function: {str(e)}")

def reduce_function():
    try:
        inverted_index = {}
        for line in sys.stdin:
            try:
                word, doc_no = line.strip().split()
                
                # Aggregate document no. for each word
                if word not in inverted_index:
                    inverted_index[word] = []
                inverted_index[word].append(doc_no)
            except ValueError:
                print(f"Unable to split the line into word and doc_no - {line}")

        # Print inverted index
        for word, doc_num in inverted_index.items():
            print(f'"{word}" {", ".join(doc_num)}')
    except Exception as e:
        print(f"Error in reduce_function: {str(e)}")

if __name__ == "__main__":
    # Input the documents
    documents = {}
    for i in range(1, 4):
        doc_text = input(f"Enter text for Document {i}: ")
        documents[f"Document {i}"] = doc_text

    try:
        
        for doc_id, doc_text in documents.items():
            map_function(doc_id, doc_text)
        
        reduce_function()
    except Exception as e:
        print(f"An error encountered: {str(e)}")
