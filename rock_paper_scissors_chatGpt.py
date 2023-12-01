import random  # استيراد مكتبة random لاختيار أرقام عشوائية

choices = ["Rock", "Paper", "Scissors"]  # قائمة تحتوي على خيارات اللعبة

def play_game():
    print("Welcome to the Rock, Paper, Scissors Game!")  # رسالة ترحيب عند بدء اللعبة

    while input("\nDo you want to play? (yes/no): ").lower() == "yes":  # هيكل التكرار يتيح للمستخدم اللعب مرارًا وتكرارًا
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()  # المستخدم يُطلب بإدخال اختياره ويتم تخزينه في user_choice
        computer_choice = random.choice(choices)  # الكمبيوتر يختار اختيارًا عشوائيًا من بين قائمة الخيارات

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        # تعبير التقييم الشرطي لتحديد الفائز
        result = "It's a tie!" if user_choice == computer_choice else "You win!" if (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ) else "Computer wins!"

        print(result)  # طباعة نتيجة الجولة

if __name__ == "__main__":
    play_game()  # تشغيل اللعبة إذا تم تشغيل الملف كبرنامج رئيسي
