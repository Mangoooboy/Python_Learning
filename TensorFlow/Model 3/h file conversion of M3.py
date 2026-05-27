# Read TFLite model

with open(
    "KL files/temperature_time_model.tflite",
    "rb"
) as f:

    tflite_model = f.read()

# Create .h file

with open(
        "KL files/model3.h",
    "w"
) as f:

    f.write("const unsigned char model_data[] = {")

    for i, byte in enumerate(tflite_model):

        if i % 12 == 0:
            f.write("\n")

        f.write(f"0x{byte:02x}, ")

    f.write("\n};\n")

    f.write(
        f"\nconst unsigned int model_data_len = {len(tflite_model)};"
    )

print("model3.h created successfully!")