import glob
import csv
import os

def decimate_file(f_in, f_out, decima):
    pass

def main():
    DECIMA = 6      # Change this for decimate exry X string

    print("Script is started")

    files = glob.glob("./input/*.txt")    

    for filepath in files:
        print("Process >> " + filepath)

        try:
            out_filepath = "./output/" + os.path.splitext(os.path.basename(filepath))[0] + "_every_" + str(DECIMA) + ".txt"
            decimate_file(filepath, out_filepath, DECIMA)
    
        except Exception as e:
            print("Cannot process >> ", filepath)
            print("Reason >> " + str(e))
            
        finally:
            print()

    print("Script is finished")

if __name__ == "__main__":
    main()