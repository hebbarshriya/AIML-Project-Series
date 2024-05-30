import sqlite3

conn = sqlite3.connect("conversation.db")


def init_db():

    conn.execute(
        """CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY,
                 usn VARCHAR UNIQUE,
                 pwd VARCHAR NOT NULL  )"""
    )

    conn.execute(
        """CREATE TABLE IF NOT EXISTS chats ( id INTEGER PRIMARY KEY,
                 usn VARCHAR, 
                 time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                 keywords VARCHAR NOT NULL,
                 data VARCHAR NOT NULL,
                 FOREIGN KEY (usn) REFERENCES users(usn))"""
    )

    conn.commit()


keywords = {
    "info": ["know", "overview", "information"],
    "benefits": ["benefits", "gains", "advantages"],
    "risks": ["loss", "uncertain", "risk"],
    "bonds": ["bonds"],
    "mutual funds": ["mutual funds"],
    "start": ["start", "begin", "options"],
    "end": ["end", "bye", "stop"],
}

answers = {
    "info": "\nInvesting is the process of allocating money or resources with the expectation of generating income or profit. It's a way to grow your wealth over time by putting your money to work for you. There are various investment options available, such as stocks, bonds, real estate, and mutual funds, each with its own risk and return profile.\n\nTo learn more about topics like benefits, bonds, risks, and mutual funds, simply type the word.\n\n ",
    "benefits": "\nInvesting can help grow your wealth over time, provide a source of passive income, and help you achieve long-term financial goals such as retirement or buying a home. Additionally, investments can help you stay ahead of inflation by generating returns that outpace rising prices.\n\nWant to learn more? Take our quick quiz to discover valuable insights!",
    "risks": "\nInvesting comes with risks, including market risk (fluctuations in asset prices), inflation risk (erosion of purchasing power over time), interest rate risk (impact of interest rate changes on investments), and specific risks related to different asset classes. It's important to understand and manage these risks through diversification, asset allocation, and a long-term investment perspective.\n\nWant to learn more? Take our quick quiz to discover valuable insights!",
    "bonds": "\nBonds are debt securities issued by governments, municipalities, or corporations to raise capital. When you buy a bond, you're essentially lending money to the issuer for a specified period, during which you receive periodic interest payments. Bonds are generally considered safer than stocks but offer lower potential returns. They can be a part of a diversified investment portfolio, balancing risk and reward\n\nWant to learn more? Take our quick quiz to discover valuable insights!",
    "mutual funds": "\nA mutual fund pools money from multiple investors to invest in a diversified portfolio of stocks, bonds, or other assets. Professional money managers handle the fund's investments, aiming to achieve specific investment objectives. Mutual funds offer diversification, liquidity, and professional management, making them popular among individual investors looking for a hands-off approach to investing.\n\nWant to learn more? Take our quick quiz to discover valuable insights!",
}

abank = {}
qbank = {
    "exp": "\nHow much experience do you have with investing? Are you a/an : \nBeginner(0) \nIntermediate(1) \nAdvanced investor(2)\n",
    "goal": "\nWhat is your main financial goal with investing? Are you looking for : \nLong-Term Growth(0) \nIncome Generation(1) \nSaving for Retirement(2) \nSaving for a Major purchase (e.g., house, car)(3) \nPreserving Wealth(4)\n",
    "risk_tol": "\nWhat is your risk tolerance? Are you comfortable with : \nHigh-Risk High-Reward Investments(0) \nModerate Risk(1) \nLow risk(2)?\n",
}


abank["goal"] = {
    0: "For long-term growth, you can invest in options like:\n - Stocks\n - Real estate\n - Mutual funds\n - ETFs\n",
    1: "For Income Generation your options can be :\n - Dividends from stocks\n - Interest from bonds\n - Rental income from real estate\n",
    2: "Saving for retirement one should have a timeline in mind which includes the period of investments and withdrawal.How much to be withdrawn at what frequency are some things to be considered.It is suggested you take some time to think about this and make a savings goal.\n",
    3: "For a major purchase one should keep in mind the when the purchase has to be made and start investing accordingly.\n",
    4: "For preserving wealth there are a variety of options such as :\n - Bonds\n - Savings accounts\n - Certificates of deposit (CDs)\n",
}
abank["exp"] = {
    0: "Since you are a beginner it is suggested to first and foremost study and get to know more about investments markets stocks etc. There are many resources available online which one can choose to their liking. Let's continue the quiz to explore your options.\n",
    1: "As an intermediate investor, you can gain deeper insights by continuing the quiz. Please answer the questions below to explore your options. To exit the chat, please type (end).\n",
    2: "Thank you for reaching out. Our chatbot is designed to provide information and basic know-how for beginner and intermediate level investors. While we focus on foundational concepts and general guidance, we understand that advanced investors may require more in-depth analysis and sophisticated strategies. If you still wish to continue, you are more than welcome to do so. To exit the chat, please type (end).\n",
}

abank["risk_tol"] = {
    0: "Some High-RIsk High-Reward options are :\n - Cryptocurrencies\n - Emerging markets\n - High-growth stocks\n",
    1: "Moderate Risks will involve a combination of high and low risk investments which will require deeper study and analysis. Mutual Funds is something which offers investments with moderate risks but one needs to study and know about the particular funds as well.\n",
    2: "Investments involving low-risk :\n - Government bonds\n - Money market funds\n - Certificates of deposit (CDs)\n",
}


def insert_user(user, passw):
    conn.execute("INSERT INTO users (usn, pwd) VALUES (?,?)", (user, passw))
    conn.commit()


def insert_chat(user, keywords, data):
    conn.execute(
        "INSERT INTO chats(usn, keywords, data) VALUES (?, ?, ?)",
        (user, keywords, data),
    )
    conn.commit()


def check_user(usn, pwd):
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM users WHERE usn=? AND pwd=?", (usn, pwd))
    if cur.fetchone()[0] == 1:
        return True
    return False


def reg(usn):
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM users WHERE usn=?", (usn,))
    users = cur.fetchone()
    if users == 1:
        return False
    return True


def print_list(user):
    cur = conn.cursor()
    cur.execute("SELECT * FROM chats WHERE usn=?", (user,))
    rows = cur.fetchall()
    num = len(rows)
    for row in rows:
        print("%d\t%s\t%s" % (row[0], row[1], row[2]))
    return num


def access_conv(user, id):
    cur = conn.cursor()
    cur.execute(
        "SELECT keywords, data FROM chats WHERE usn = ? AND  id = ?",
        (
            user,
            id,
        ),
    )
    return cur.fetchone()


def ques():
    j = ""
    for key, q in qbank.items():
        ans = int(input(q)+ "\n")
        while ans>=len(abank[key]):
            print("Please choose 1 of the provided options: ")
            ans = int(input(q)+ "\n")
        print(abank[key][ans])
        j += key + ":" + str(ans) + ";"
    return j


def new_conv(usn):
    print(
        "Hello and welcome to our Investment Assistant Chatbot! Whether you're a beginner just starting your investment journey or an intermediate investor looking to expand your knowledge, we're here to help. \n\nOur chatbot provides information and guidance on a range of investment topics to support your financial goals. If you're an advanced investor seeking more sophisticated strategies, please note that our focus is on basic concepts and general advice. However, you are welcome to explore and ask questions. To exit the chat at any time, simply type (end). To look at your investing options you can start the quiz(start)\n\nLet's get started! How can I assist you today?\n"
    )
    i = 0
    k = ""  # questions asked
    j = ""
    while i < 12:
        c = 0
        print(">>>", end=" ")
        question = input()
        for key, words in keywords.items():
            for word in words:
                if word in question.lower():
                    c = 1
                    if key == "start":
                        j = ques()
                        break
                    elif key == "end":
                        insert_chat(usn, k, j)
                        print("Hope this coversation was helpful. Have a great day!")
                        return
                    else:
                        print(answers[key] + "\n")
                        k += key + ";"
                        break
            if c == 1:
                break
        if c == 0:
            print("Didnt understand the question. Please rephrase.\n")
        i += 1
    print("Limit for this conversation has been reached. Please start a new conversation\n")


def cont_conv(usn, chat):
    row = access_conv(usn, chat)
    k, data = row
    q = k.strip().split(";")
    for i in q:
        if i:
            print(i, "\n", answers[i], "\n")
    dat = data.strip().split(";")
    for q in dat:
        print(q)
        if ":" in q:
            i, j = q.split(":")
            if j:
                print(i, " - ", abank[i][int(j)])

    print("Your previous conversation has been loaded. How can I help you?\n")
    i = 0
    while i < 12:
        c = 0
        print(">>>", end=" ")
        question = input()
        for key, words in keywords.items():
            for word in words:
                if word in question.lower():
                    c = 1
                    if key == "end":
                        insert_chat(usn, k, data)
                        print("Hope this coversation was helpful. Have a great day!")
                        return
                    elif key=="start" and data :
                        print("You have already taken the quiz.\n")
                        break
                    else:
                        print(answers[key])
                        if key not in k:
                            k += key + ";"
                        break
            if c == 1:
                break
        if c == 0:
            print("Didnt understand the question. Please rephrase.\n")
        i += 1
    print("Limit for this conversation has been reached. Please start a new conversation\n")


def run():
    print("\n(Enter -1 to for new user registration)\n\nEnter Username : ")
    usn = input()
    if usn == "-1":
        while 1:
            usn = input("Enter Username: ")
            if reg(usn):
                pwd = input("Enter Password: ")
                insert_user(usn, pwd)
                break
            else:
                print("Username already exists. Try again.")
                continue
    else:
        pwd = input("Enter Password: ")

    if check_user(usn, pwd):
        print("\nLogin successful!\n")
        type = int(input("New Chat(1) or continue previous conversation(2)? : "))
        if type == 1:
            new_conv(usn)
        else:
            num = print_list(usn)
            if num == 0:
                print("No previous conversations found.You can start a new chat.\n")
                new_conv(usn)
            else:
                print("Choose conversation to continue.")
                chat = int(input())
                cont_conv(usn, chat)

    else:
        print("Wrong usename or password.")


if __name__ == "__main__":
    init_db()
    run()
