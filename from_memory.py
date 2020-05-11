import hashlib
import time
# input_path = 'data_embrions/focal1.tif'
# output_path = 'data.out'
input_path = '/mnt/lsdf_carlo/Carlo Beretta/Ariel Rivas/focal1.tif'# input('introduce input file:')
output_path = '/mnt/lsdf_carlo/Carlo Beretta/Ariel Rivas/data.out'# input('introduce input file:')

reading_time = 0
processing_time = 0
writing_time = 0
t_initial = time.time()
for _ in range(100):
    with open(input_path,'rb') as f:
        import hashlib
        # reading
        t0 = time.time()
        data = f.read()
        reading_time += time.time() - t0
        # processing
        t0 = time.time()
        m = hashlib.sha256()
        m.update(data)
        m.digest()
        processing_time += time.time() - t0
        # writing
        t0 = time.time()
        with open(output_path, 'wb') as f2:
            f2.write(data)
        writing_time += time.time() - t0

print('performance: reading ', reading_time/100, ' write ', writing_time/100, ' processing time ', processing_time/100)

