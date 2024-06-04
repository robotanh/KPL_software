from KPL_MySQL_header import *


def main():
    # ma_lan_bom_array=[1,1,1,1,1,1,1]
    # for i in range (1,701):
    #     rand_id_voi_bom=random.randint(1,7)
    #     faking_data(rand_id_voi_bom,ma_lan_bom_array[rand_id_voi_bom-1])
    #     ma_lan_bom_array[rand_id_voi_bom-1]+=1
    data={
        "id_voi":1,
        "ma_lan_bom":2,
        "gia_ban":25000,
        "tong_da_bom":5,
        "tien_ban":125000
    }
    filtered_insert(data)


if __name__ == "__main__":
    main()


