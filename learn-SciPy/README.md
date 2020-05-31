# Python系列教程——SciPy稀疏矩阵



```python
from scipy.sparse import bsr_matrix
data = np.array([[1, 2, 3, 4]]).repeat(3, axis=0)
offsets = np.array([0, -1, 2])
dia_matrix((data, offsets), shape=(4, 4)).toarray()
```



```python
from scipy.sparse import dia_matrix
data = np.array([[1, 2, 3, 4]]).repeat(3, axis=0)
offsets = np.array([0, -1, 2])
dia_matrix((data, offsets), shape=(4, 4)).toarray()
```



```
data = np.arange(6).reshape(2,3)+1
mtx[:2,[1,2,3]] = data
mtx.toarray()
print(mtx)
```

