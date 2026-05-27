with open(
    "Trained Models/temperature_model2.tflite",
    "rb"
) as f:

    model = f.read()

with open(
    "Trained Models/model2.h",
    "w"
) as f:

    f.write("const unsigned char model_data[] = {")

    for i, byte in enumerate(model):

        if i % 12 == 0:
            f.write("\n")

        f.write(f"0x{byte:02x}, ")

    f.write("\n};\n")

print("model2.h created successfully!")