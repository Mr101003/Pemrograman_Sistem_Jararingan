import multiprocessing as mp
def my_function(seconds):
    
    T1 = time.perf_counter()
    time.sleep(seconds)
    T2 = time.perf_counter()
    return T2-T1
    
if __name__ == '__main__':
    T1 = time.perf_counter()
    pool = mp.Pool(processes=4)
    results = pool.map_async(my_function,[4,1,3,2])
    results.wait()
    no = 1
    for duration in results.get():
        print(f"Process {no}  (%.2f detik)"%duration)
        no = no + 1
        
    T2 = time.perf_counter()
    print('Selesai dalam %.2f detik'%(T2-T1))
