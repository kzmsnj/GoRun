# Centroid Binary Feature (Hamming) - [Tidur > 7 Jam, Cuaca Cerah, Bebas Nyeri Otot]
rest_class_centroids = {
    "Lari Hari Ini": [1, 1, 1],
    "Istirahat Total": [0, 0, 0]
}

def calculate_hamming_distance(feature_x, centroid_m):
    distance = 0
    for i in range(len(feature_x)):
        distance += feature_x[i] ^ centroid_m[i]
    return distance

def get_binary_input(prompt):
    while True:
        val = input(prompt + " (1=Ya, 0=Tidak): ")
        if val in ['0', '1']: 
            return int(val)

def jalankan_menu():
    print("\n--- MENU 2: Kesiapan Fisik (Hamming Distance) ---")
    f1 = get_binary_input("Tidur lebih dari 7 jam semalam?")
    f2 = get_binary_input("Cuaca cerah/mendukung?")
    f3 = get_binary_input("Badan segar (bebas nyeri)?")
    feature_vector = [f1, f2, f3]
    
    distances = {}
    for class_name, centroid in rest_class_centroids.items():
        dist = calculate_hamming_distance(feature_vector, centroid)
        distances[class_name] = dist
    
    predicted_class = min(distances, key=distances.get)
    print(f"\n=> KESIMPULAN: Sistem menyarankan ** {predicted_class.upper()} **")