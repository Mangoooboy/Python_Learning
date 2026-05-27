# Read .tflite file
with open("Trained Models/temperature_model.tflite", "rb") as f:
    model_data = f.read()

# Create header file
with open("Trained Models/model.h", "w") as f:
    f.write("const unsigned char model[] = {\n")

    for i, byte in enumerate(model_data):
        f.write(f"0x{byte:02x},")

        if (i + 1) % 12 == 0:
            f.write("\n")

    f.write("\n};\n")

    f.write(f"const unsigned int model_len = {len(model_data)};\n")

print("model.h created successfully!")