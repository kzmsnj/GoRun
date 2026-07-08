import math

# Centroid Minimum Distance (Euclidean) - [Jarak (km), Pace (desimal)]
run_class_centroids = {
    "Recovery Run": [3.0, 7.50],
    "Tempo Run": [5.0, 5.50],
    "Long Run": [10.0, 6.50]
}

def pace_to_decimal(pace_str):
    try:
        minutes, seconds = map(int, pace_str.split(':'))
        return minutes + (seconds / 60.0)
    except ValueError:
        print("Format salah. Menggunakan default 0.0")
        return 0.0

def calculate_euclidean_distance(feature_x, centroid_m):
    jarak_diff = feature_x[0] - centroid_m[0]
    pace_diff = feature_x[1] - centroid_m[1]
    return math.sqrt((jarak_diff ** 2) + (pace_diff ** 2))

def jalankan_menu():
    print("\n--- MENU 1: Tipe Lari (Euclidean Distance) ---")
    input_jarak = input("Jarak tempuh (km) [default 4.37]: ") or "4.37"
    input_pace = input("Pace (MM:SS) [default 5:44]: ") or "5:44"
    
    jarak_km = float(input_jarak)
    pace_dec = pace_to_decimal(input_pace)
    feature_vector = [jarak_km, pace_dec]
    
    distances = {}
    for class_name, centroid in run_class_centroids.items():
        dist = calculate_euclidean_distance(feature_vector, centroid)
        distances[class_name] = dist
    
    predicted_class = min(distances, key=distances.get)
    print(f"\n=> KESIMPULAN: Sesi larimu diklasifikasikan sebagai ** {predicted_class.upper()} **")