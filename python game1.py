import random

# কম্পিউটার ১ থেকে ১০ এর মধ্যে একটি র্যান্ডম সংখ্যা সিলেক্ট করবে
computer_number = random.randint(1, 10)

print("১ থেকে ১০ এর মধ্যে একটি সংখ্যা অনুমান করো!")

while True:
    # ইউজারের কাছ থেকে ইনপুট নেওয়া
    user_guess = int(input("তোমার অনুমান লেখো: "))
    
    # লজিক চেক করা
    if user_guess == computer_number:
        print("অভিনন্দন! তোমার অনুমান একদম সঠিক হয়েছে। 🎉")
        break  # অনুমান মিলে গেলে গেম শেষ
    elif user_guess < computer_number:
        print("উঁহু! একটু বড় সংখ্যা চেষ্টা করো। ⬆️")
    else:
        print("উঁহু! একটু ছোট সংখ্যা চেষ্টা করো। ⬇️")