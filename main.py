from conference import Conference


def main():
    first_conference = Conference("Python Conference", 100, 1000, "New York", "2021-10-10", "Python Software Foundation")
    second_conference = Conference("Java Conference", 200, 2000, "San Francisco", "2021-10-20", "Java Community")
    third_conference = Conference("JavaScript Conference", 300, 3000, "Los Angeles", "2021-10-30", "JavaScript Community")
    print(f"First Conference: {first_conference}\nSecond Conference: {second_conference}\nThird Conference: {third_conference}")



if __name__ == "__main__":
    main()