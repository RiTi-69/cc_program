import datetime
import os

def main():
    # The classic greeting
    print("\n" + "="*30)
    print("Hello, World!")
    print("="*30)
    
    # Adding some useful context for Cloud Shell
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    user = os.getenv('USER', 'Developer')
    
    print(f"User: {user}")
    print(f"Time: {current_time}")
    print("Execution: Successful")
    print("="*30 + "\n")

if __name__ == "__main__":
    main()
