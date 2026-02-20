import sweph as swe

def main():
    try:
        sun_calc_ut = swe.calc_ut(2461072.0, 0)

        print("--- Sun Position with calc_ut() ---")
        print(f"Longitude: {sun_calc_ut['longitude']:.4f}")
        print(f"Latitude:  {sun_calc_ut['latitude']:.4f}")
        print(f"Distance:  {sun_calc_ut['distance']:.4f} AU")

    except RuntimeError as e:
        print(f"SwissEph Error: {e}")

if __name__ == "__main__":
    main()
