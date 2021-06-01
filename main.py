import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Streamlit 入門')
st.write('Data Frame')

df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df3)

st.write('プレグレスバー')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done'

left_column, right_column = st.beta_columns(2)

button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラムです')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は', option , "です"

# option2 = st.text_input('あなたの趣味を教えて下さい')
# 'あなたの趣味は', option2 , "です"

# condition = st.slider('あなたの調子は？', 0, 100, 15)
# 'コンディション：', condition