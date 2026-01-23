from PIL import Image

def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_image)
    print("Encryption completed successfully!")


def decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_image)
    print("Decryption completed successfully!")


if __name__ == "__main__":
    print("Pixel Manipulation Image Encryption")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Enter your choice (1 or 2): ")
    key = int(input("Enter encryption key (number): "))

    if choice == "1":
        input_img = input("Enter input image name (with extension): ")
        output_img = "encrypted_image.png"
        encrypt_image(input_img, output_img, key)

    elif choice == "2":
        input_img = input("Enter encrypted image name: ")
        output_img = "decrypted_image.png"
        decrypt_image(input_img, output_img, key)

    else:
        print("Invalid choice!")
