# Python系列教程——SciPy稀疏矩阵

## 1. 稀疏矩阵存储格式Storage Schemes

### 1.1 COO坐标格式 (Coordinate Format)

**COO坐标格式优势在于：简单快速创建；转换为其他格式；快速矩阵向量积**

**COO坐标格式劣势在于：不支持矩阵切片**

#### 1.1.1 创建COO空矩阵

```python
from scipy import sparse
mtx = sparse.coo_matrix((3, 4), dtype=np.int8)
```

#### 1.1.2 创建COO稀疏矩阵

In[]:

```python
import numpy as np
from scipy import sparse

row = np.array([0, 3, 1, 0])
col = np.array([0, 3, 1, 2])
val = np.array([4, 5, 7, 9])
mtx = sparse.coo_matrix((val, (row, col)), shape=(4, 4))

print(mtx)
```

Out[]:

```
  (0, 0)	4
  (3, 3)	5
  (1, 1)	7
  (0, 2)	9
```

In[]:

```python
matrix_mtx = mtx.todense()
matrix_mtx
```

Out[]:

```
matrix([[4, 0, 9, 0],
        [0, 7, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 5]])
```

In[]:

```python
array_mtx = mtx.toarray()
array_mtx
```

Out[]:

```
array([[4, 0, 9, 0],
       [0, 7, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 5]])
```

#### 1.1.3参数解释

(1) row为矩阵中元素对应的行数

(2) col为矩阵中元素对应的列数

(3) val为矩阵中对应行列的元素值

### 1.2 DIR对角格式 (Diagonal Format)

**DIR坐标格式优势在于：简单快速创建；快速矩阵向量积；numpy向量运算**

**COO坐标格式劣势在于：远离对角线的元素填充造成内存资源浪费；不支持矩阵切片**

#### 1.2.1创建DIR稀疏矩阵

In[]:

```python
from scipy.sparse import dia_matrix
data = np.arange(12).reshape(3,4)+1
offsets = np.array([0, -1, 2])
mtx = dia_matrix((data, offsets), shape=(4, 4))
print(mtx)
```

Out[]:

```
  (0, 0)	1
  (1, 1)	2
  (2, 2)	3
  (3, 3)	4
  (1, 0)	5
  (2, 1)	6
  (3, 2)	7
  (0, 2)	11
  (1, 3)	12
```

In[]:

```python
mtx.toarray()
```

Out[]:

```
array([[ 1,  0, 11,  0],
       [ 5,  2,  0, 12],
       [ 0,  6,  3,  0],
       [ 0,  0,  7,  4]])
```

#### 1.2.2解释参数

```
offset: row

     2:  9
     1:  --10------
     0:  1  . 11  .
    -1:  5  2  . 12
    -2:  .  6  3  .
    -3:  .  .  7  4
         ---------8
```

#### 1.2.3矩阵运算

In[]:

```python
vec = np.ones((4,1 ))
mat*vec
```

Out[]:

```
array([[12.],
       [19.],
       [ 9.],
       [11.]])
```

### 1.3 CSR行压缩格式 (Compressed Sparse Row Format)

**CSR行压缩格式优势在于：高效的运算速度；行切片效率高；快速矩阵向量积**

**CSR行压缩格式劣势在于：列切片效率低；转换为其他稀疏矩阵格式代价高**

#### 1.3.1 创建CSR稀疏矩阵

**方法一：**

In[]:

```
import numpy as np
from scipy import sparse
data = np.array([1, 2, 3, 4, 5, 6])
indices = np.array([0, 2, 2, 0, 1, 2])
indptr = np.array([0, 2, 3, 6])
mtx = sparse.csr_matrix((data, indices, indptr), shape=(3, 3))
mtx.todense()
```

Out[]:

```
matrix([[1, 0, 2],
        [0, 0, 3],
        [4, 5, 6]])
```

**方法二：**

In[]:

```
import numpy as np
from scipy.sparse import csr_matrix

row = np.array([0, 0, 1, 2, 2, 2])
col = np.array([0, 2, 2, 0, 1, 2])
data = np.array([1, 2, 3, 4, 5, 6])
csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
```

Out[]:

```python
array([[1, 0, 2],
       [0, 0, 3],
       [4, 5, 6]])
```

#### 1.3.2 参数解释

(1) data为CSR稀疏矩阵中的所有非零元素，先从左至右检索第一行中的所有元素，再检索第二行、第三行、、、直至结束，将所有元素存储在一个向量中；

(2) indices为CSR稀疏矩阵中data各元素对应的列号，比如其中的1为data中元素5对应的列索引号；

(3) indptr最难理解，首先，indptr为一向量，元素个数为mtx矩阵的行数+1，这里mtx行数为3，所以indptr的元素数量为3+1=4，其次，indptr中第一个元素为0，第二个元素为mtx矩阵中第一行非零元素的总数，第三个元素为mtx矩阵中前两行非零元素的总数，第四个元素为mtx矩阵中前三行非零元素的总数，依次类推...

### 1.4 CSC列压缩格式（Compressed Sparse Column Format )

**CSC列压缩格式优势在于：高效的运算速度；列切片效率高；快速矩阵向量积**

**CSC列压缩格式劣势在于：行切片效率低；转换为其他稀疏矩阵格式代价高**

#### 1.4.1 创建CSC列压缩格式稀疏矩阵

**方法一**

In[]:

```python
import numpy as np
from scipy import sparse
data = np.array([1, 1, 2, 3, 4, 5, 6])
indices = np.array([0, 2, 0, 2, 0, 1, 2])
indptr = np.array([0, 2, 4, 7])
mtx = sparse.csc_matrix((data, indices, indptr), shape=(3, 3))
mtx.todense()
```

Out[]:

```python
matrix([[1, 2, 4],
        [0, 0, 5],
        [1, 3, 6]])
```

**方法二**

In[]:

```python
import numpy as np
from scipy import sparse
row = np.array([0, 0, 0, 1, 2, 2, 2])
col = np.array([0, 1, 2, 2, 0, 1, 2])
data = np.array([1, 2, 4, 5, 1, 3, 6])
mtx = sparse.csc_matrix((data, (row, col)), shape=(3, 3))

mtx.todense()
```

Out[]:

```python
matrix([[1, 2, 4],
        [0, 0, 5],
        [1, 3, 6]], dtype=int32)
```

#### 1.4.2 参数解释

(1) data为CSC稀疏矩阵中的所有非零元素，先从上至下检索第一列中的所有元素，再检索第二列、第三列、、、直至结束，将所有元素存储在一个向量中；

(2) indices为CSC稀疏矩阵中data各元素对应的行号，比如其中的1为data中元素5对应的行索引号；

(3) indptr最难理解，首先，indptr为一向量，元素个数为mtx矩阵的列数+1，这里mtx列数为3，所以indptr的元素数量为3+1=4，其次，indptr中第一个元素为0，第二个元素为mtx矩阵中第一列非零元素的总数，第三个元素为mtx矩阵中前两列非零元素的总数，第四个元素为mtx矩阵中前三列非零元素的总数，依次类推...



### 1.5 BSR分块压缩格式 (Block Compressed Row Format)

**BSR分块压缩格式优势在于：高效的运算速度；快速矩阵向量积**

**BSR分块压缩格式劣势在于：**

#### 1.5.1创建BSR分块压缩行格式稀疏矩阵

##### 方法一

Int[]:

```python
import numpy as np
from scipy import sparse

indptr = np.array([0, 2, 3, 5])
indices = np.array([0, 2, 2, 1, 2])
data = np.array([1, 2, 3, 4, 5]).repeat(4).reshape(5, 2, 2)
mtx = sparse.bsr_matrix((data, indices, indptr), shape=(6, 6))
mtx.todense()
```

Out[]:

```python
matrix([[1, 1, 0, 0, 2, 2],
        [1, 1, 0, 0, 2, 2],
        [0, 0, 0, 0, 3, 3],
        [0, 0, 0, 0, 3, 3],
        [0, 0, 4, 4, 5, 5],
        [0, 0, 4, 4, 5, 5]])
```

In[]:

```
mtx.data
```

Out[]:

```
array([[[1, 1],
        [1, 1]],

       [[2, 2],
        [2, 2]],

       [[3, 3],
        [3, 3]],

       [[4, 4],
        [4, 4]],

       [[5, 5],
        [5, 5]]])
```

In[]:

```
mtx.indices
```

Out[]:

```
array([0, 2, 2, 1, 2])
```

In []:

```
mtx.shape
```

Out[]:

```
(6, 6)
```

In []:

```
mtx.blocksize
```

Out[]:

```
(2, 2)
```

In []:

```
mtx.indptr
```

Out[]:

```
array([0, 2, 3, 5])
```

##### 方法二

In[]:

```
row = np.array([0, 0, 1, 2, 2, 2])
col = np.array([0, 2, 2, 0, 1, 2])
data = np.array([1, 2, 3, 4, 5, 6])
mtx = sparse.bsr_matrix((data, (row, col)), shape=(3, 3))

mtx  

mtx.todense()   

mtx.data    

mtx.indices

mtx.indptr
```

#### 1.5.2参数解释

(1) data为BSR稀疏矩阵中的所有非零子块矩阵，先从左至右检索第一行中的所有子块矩阵，再检索第二行、第三行、、、直至结束，将所有子块矩阵存储在一个data矩阵中；

(2) indices为BSR稀疏矩阵中data各子块矩阵对应的列号，比如其中的1为data中子块矩阵   [[4, 4],  [4, 4]],对应的列索引号；

(3) indptr最难理解，首先，indptr为一向量，元素个数为mtx矩阵的行数/子块矩阵行数+1，这里mtx行数为6，子块矩阵行数为2，所以indptr的元素数量为6/2+1=4，其次，indptr中第一个元素为0，第二个元素为mtx矩阵中第一行非零子块的总数，第三个元素为mtx矩阵中前两行非零子块的总数，第四个元素为mtx矩阵中前三行非零子块的总数，依次类推...

### 1.6 LIL列表格式(List of Lists Format)

**LIL列表格式优势在于：便于增量式创建稀疏矩阵；花式索引切片；便于存储格式转换；适用于数据未知**

**LIL列表格式劣势在于：计算效率低；行切片效率低**

#### 1.6.1创建LIL型稀疏矩阵

In[]:

```python
import numpy as np
from scipy import sparse
data = np.arange(6).reshape(2, 3)+1
mtx = sparse.lil_matrix((4, 5))
mtx[:2, [1, 2, 3]] = data

mtx.todense()
mtx.toarray()
```

Out[]:

```
array([[0., 1., 2., 3., 0.],
       [0., 4., 5., 6., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
```

#### 1.6.2花式索引切片

In[]:

```python
mtx[:2, :].todense()
```

Out[]:

```
matrix([[0., 1., 2., 3., 0.],
        [0., 4., 5., 6., 0.]])
```

### 1.7 DOK键字典格式(Dictionary of Keys Format)

**DOK键字典格式优势在于：自由快速切片；快速转换格式；适用于矩阵元素事先未知**

**DOK键字典格式劣势在于：计算效率低；不允许索引重复**

#### 1.7.1创建空稀疏矩阵

```python
mtx = sparse.dok_matrix((5, 5), dtype=np.float64)
```

#### 1.7.2以元素建立矩阵

Int[]:

```python
from scipy import sparse
mtx = sparse.dok_matrix((5, 5), dtype=np.float64)

for ir in range(5):
    for ic in range(5):
        mtx[ir, ic] = 1.0 * (ir != ic)

array_mtx = mtx.toarray()
array_mtx
```


Out[]:

```
array([[0., 1., 1., 1., 1.],
       [1., 0., 1., 1., 1.],
       [1., 1., 0., 1., 1.],
       [1., 1., 1., 0., 1.],
       [1., 1., 1., 1., 0.]])
```

```
matrix_mtx = mtx.todense()
matrix_mtx 
```

Out[]:

```
matrix([[0., 1., 1., 1., 1.],
        [1., 0., 1., 1., 1.],
        [1., 1., 0., 1., 1.],
        [1., 1., 1., 0., 1.],
        [1., 1., 1., 1., 0.]])
```

Int[]:

```python
mtx[[2,1], 1:3].todense()
```

Out[]:

```python
matrix([[1., 0.],
        [0., 1.]])
```





## 参考文献

1. https://scipy-lectures.org/advanced/scipy_sparse/index.html

2. https://docs.scipy.org/doc/scipy/reference/sparse.html