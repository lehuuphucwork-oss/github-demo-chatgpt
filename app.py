def greet(name, language="en"):
    if language == "en":
        print(f"Hello, {name}!")
        print("This is version 2 of our app.")
        print("Have a nice day!")
    elif language == "vi":
        print(f"Xin chào, {name}!")
        print("Đây là phiên bản 2 của ứng dụng.")
        print("Chúc bạn một ngày tốt lành!")
    else:
        print(f"Hello, {name} (language not supported).")

if __name__ == "__main__":
    greet("Phuc", "vi")
