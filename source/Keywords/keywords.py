def main():
    n = int(input())
    keywords_normalized = []
    for i in range(n):
        keywords_normalized.append(input().lower().replace("-", " "))
    print(len(set(keywords_normalized)))

if __name__ == "__main__":
    main()