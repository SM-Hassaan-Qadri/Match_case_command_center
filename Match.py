import time 
import datetime
import random
timestamp = time.strftime("%H : %M : %S")

today = datetime.date.today()

command = input("Hello There What To Do Today >").lower()

language = input("Enter Your Language >").lower()

jokes_english = [
    "Why do programmers hate nature? Too many bugs.",
    "Why do Python devs wear glasses? Because they can't C.",
    "I told my computer I needed a break, and it said 'No problem, I^ll go to sleep.'"
]

jokes_Japanese = [
    "プログラマーが自然を嫌う理由は？バグが多すぎるから",
    "なぜPython開発者はメガネをかけるの？Cが見えないから。" , 
    "コンピューターに休憩が必要だと言ったら、「問題ない、スリープモードに入るよ」と言われた。"
]

jokes_Korean = [
       "프로그래머들이 자연을 싫어하는 이유는? 벌레(버그)가 너무 많아서요" , 
       "왜 파이썬 개발자들은 안경을 쓸까요? C를 볼 수 없으니까요." ,
       "컴퓨터에게 휴식이 필요하다고 말했더니, “문제 없어, 나는 잠들게.”라고 했어요.." 
]

jokes_Urdu = [
       "پروگرامرز قدرت سے کیوں نفرت کرتے ہیں؟ کیونکہ وہاں بہت زیادہ بگز ہوتے ہیں" , 
       " نہیں دیکھ سکتے 'C' ۔ڈویلپر چشمہ کیوں پہنتے ہیں؟ کیونکہ وہ" ,
       "میں نے اپنے کمپیوٹر سے کہا مجھے آرام چاہیے، اس نے کہا کوئی مسئلہ نہیں، میں سونے جا رہا ہوں۔"
]

jokes_hindi = [
        "प्रोग्रामर प्रकृति से नफरत क्यों करते हैं? क्योंकि वहाँ बहुत सारे बग्स होते हैं।" ,
        "Python डिवेलपर्स चश्मा क्यों पहनते हैं? क्योंकि वे C नहीं देख सकते।" ,
        "मैंने अपने कंप्यूटर से कहा कि मुझे ब्रेक चाहिए, उसने कहा कोई बात नहीं, मैं सोने जा रहा हूँ।"
]

match command :
   
    case "greet" if language == "english" :
          print("Hi there user welcome ")

    case "greet" if language == "korean" :
          print("안녕하세요 사용자 환영합니다")
 
    case "greet" if language == "japanese" :
          print("こんにちは、ユーザーさん、ようこそ")

    case "greet" if language == "urdu" :
            print("خوشامدین گہک")

    case "greet" if language == "hindi" :
            print("खुशामदीन गाहक")
    
    case "greet" if language == "arabic" :
              print("مرحبًا بك، نرحب بالمستخدم")

    case "time" :
          print(timestamp)

    case "date" :
            print(today)  

    case "jokes" if language == "english" :
            print(random.choice(jokes_english))     

    case "jokes" if language == "japanese" :
              print(random.choice(jokes_Japanese))

    case "jokes" if language == "korean" :
              print(random.choice(jokes_Korean))

    case "jokes" if language == "urdu" :
              print(random.choice(jokes_Urdu))

    case "jokes" if language == "hindi" :
              print(random.choice(jokes_hindi))

    case _:
          print("Welcome to Match Case Command Center. This Command Centre can do following task \
            \n Greet user based on their language (enter greet as input) \
            \n Show current Time of user device (enter Time as input) \
            \n Shows Date of user (enter date as input) \
            \n Tells a joke (enter jokes as input )")
