import swisseph as swe

def main():
    try:
        sun_calc = swe.calc(2461072.0, 0)

        print("--- Sun Position with calc() ---")
        print(f"Longitude: {sun_calc['longitude']:.4f}°")
        print(f"Latitude:  {sun_calc['latitude']:.4f}°")
        print(f"Distance:  {sun_calc['distance']:.4f} AU")

        sun_calc_ut = swe.calc_ut(2461072.0, 0)

        print("--- Sun Position with calc_ut() ---")
        print(f"Longitude: {sun_calc_ut['longitude']:.4f}°")
        print(f"Latitude:  {sun_calc_ut['latitude']:.4f}°")
        print(f"Distance:  {sun_calc_ut['distance']:.4f} AU")

        version = swe.version()
        print(f"SwissEph Version: {version}")

    except RuntimeError as e:
        print(f"SwissEph Error: {e}")

if __name__ == "__main__":
    main()
