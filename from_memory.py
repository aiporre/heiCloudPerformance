import hashlib
import time
input_path = input('introduce input file:')
output_path = 'data.out'

reading_time = 0
processing_time = 0
writing_time = 0
t_initial = time.time()
for _ in range(100):
    with open(input_path) as f:
        import hashlib
        # reading
        t0 = time.time()
        data = f.read()
        reading_time = time.time() - t0
        # processing
        t0 = time.time()
        m = hashlib.sha256()
        m.update(data)
        m.digest()
        processing_time = time.time() - t0
        # writing
        t0 = time.time()
        with open(output_path) as f2:
            f2.write(data)
        writing_time = time.time() - t0

print('performance: reading ', reading_time, ' write ', writing_time, ' processing time ', processing_time)

