from KPL_MySQL_header import *


def main():
    ma_lan_bom_array=[1,1,1,1,1,1,1]
    for i in range (1,701):
        rand_id_voi_bom=random.randint(1,7)
        faking_data(rand_id_voi_bom,ma_lan_bom_array[rand_id_voi_bom-1])
        ma_lan_bom_array[rand_id_voi_bom-1]+=1


if __name__ == "__main__":
    main()


