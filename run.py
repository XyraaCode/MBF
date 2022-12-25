import os
if __name__ == "__main__":
        try:
                __import__("mbf").cek_lisensi_aktif()
        except Exception as e:
                exit(str(e))