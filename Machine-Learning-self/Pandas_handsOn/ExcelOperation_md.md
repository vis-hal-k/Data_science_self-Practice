<div style = "  display : flex; justify-content: center; ">
    <h1 style = " background-color: Black; color:white; display:flex; padding:10px"> Pandas Hands On</h1>
 </div>


```python
import pandas as pd
import numpy as np
print(pd.__version__)
ds = pd.read_excel('ExcelFile/Pandas.xlsx')
ds
```

    1.4.2
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Howrah</td>
    </tr>
    <tr>
      <th>1</th>
      <td>30</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40</td>
      <td>NaN</td>
      <td>Vishal</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>50</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
ds.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4 entries, 0 to 3
    Data columns (total 4 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   10          4 non-null      int64  
     1   Unnamed: 1  0 non-null      float64
     2   Unnamed: 2  1 non-null      object 
     3   Unnamed: 3  1 non-null      object 
    dtypes: float64(1), int64(1), object(2)
    memory usage: 256.0+ bytes
    


```python
ds.head(1) # it is used to show number of rows from beginning.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Howrah</td>
    </tr>
  </tbody>
</table>
</div>




```python
ds.tail(2) # it is to used to show number of rows from End .
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>40</td>
      <td>NaN</td>
      <td>Vishal</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>50</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
dss = ds.fillna(value= 0) # to set the Null value
dss
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>0.0</td>
      <td>0</td>
      <td>Howrah</td>
    </tr>
    <tr>
      <th>1</th>
      <td>30</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40</td>
      <td>0.0</td>
      <td>Vishal</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>50</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## Slicing


```python
ds1 = pd.read_excel('ExcelFile/2023_BATCH_PLACEMENT_CIVIL.xlsx')
zm = pd.read_csv('ExcelFile/zomato.csv')
zm
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>Jalsa</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>Spice Elephant</td>
      <td>Yes</td>
      <td>No</td>
      <td>4.1/5</td>
      <td>787</td>
      <td>080 41714161</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>
      <td>Chinese, North Indian, Thai</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  Had been here for din...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>San Churro Cafe</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>918</td>
      <td>+91 9663487993</td>
      <td>Banashankari</td>
      <td>Cafe, Casual Dining</td>
      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>
      <td>Cafe, Mexican, Italian</td>
      <td>800</td>
      <td>[('Rated 3.0', "RATED\n  Ambience is not that ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>
      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>
      <td>Addhuri Udupi Bhojana</td>
      <td>No</td>
      <td>No</td>
      <td>3.7/5</td>
      <td>88</td>
      <td>+91 9620009302</td>
      <td>Banashankari</td>
      <td>Quick Bites</td>
      <td>Masala Dosa</td>
      <td>South Indian, North Indian</td>
      <td>300</td>
      <td>[('Rated 4.0', "RATED\n  Great food and proper...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>Grand Village</td>
      <td>No</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>166</td>
      <td>+91 8026612447\r\n+91 9901210005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Panipuri, Gol Gappe</td>
      <td>North Indian, Rajasthani</td>
      <td>600</td>
      <td>[('Rated 4.0', 'RATED\n  Very good restaurant ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51712</th>
      <td>https://www.zomato.com/bangalore/best-brews-fo...</td>
      <td>Four Points by Sheraton Bengaluru, 43/3, White...</td>
      <td>Best Brews - Four Points by Sheraton Bengaluru...</td>
      <td>No</td>
      <td>No</td>
      <td>3.6 /5</td>
      <td>27</td>
      <td>080 40301477</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', "RATED\n  Food and service are ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51713</th>
      <td>https://www.zomato.com/bangalore/vinod-bar-and...</td>
      <td>Number 10, Garudachar Palya, Mahadevapura, Whi...</td>
      <td>Vinod Bar And Restaurant</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>+91 8197675843</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>600</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51714</th>
      <td>https://www.zomato.com/bangalore/plunge-sherat...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Plunge - Sheraton Grand Bengaluru Whitefield H...</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>2,000</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51715</th>
      <td>https://www.zomato.com/bangalore/chime-sherato...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Chime - Sheraton Grand Bengaluru Whitefield Ho...</td>
      <td>No</td>
      <td>Yes</td>
      <td>4.3 /5</td>
      <td>236</td>
      <td>080 49652769</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar</td>
      <td>Cocktails, Pizza, Buttermilk</td>
      <td>Finger Food</td>
      <td>2,500</td>
      <td>[('Rated 4.0', 'RATED\n  Nice and friendly pla...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51716</th>
      <td>https://www.zomato.com/bangalore/the-nest-the-...</td>
      <td>ITPL Main Road, KIADB Export Promotion Industr...</td>
      <td>The Nest - The Den Bengaluru</td>
      <td>No</td>
      <td>No</td>
      <td>3.4 /5</td>
      <td>13</td>
      <td>+91 8071117272</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>NaN</td>
      <td>Finger Food, North Indian, Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', 'RATED\n  Great ambience , look...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
  </tbody>
</table>
<p>51717 rows × 17 columns</p>
</div>




```python
#slicing 
display(zm[1:5])
display(zm.loc[[100,4,5,6]])
display(zm.iloc[1:10 , 0:3])  # This is for both row and column
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>Spice Elephant</td>
      <td>Yes</td>
      <td>No</td>
      <td>4.1/5</td>
      <td>787</td>
      <td>080 41714161</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>
      <td>Chinese, North Indian, Thai</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  Had been here for din...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>San Churro Cafe</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>918</td>
      <td>+91 9663487993</td>
      <td>Banashankari</td>
      <td>Cafe, Casual Dining</td>
      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>
      <td>Cafe, Mexican, Italian</td>
      <td>800</td>
      <td>[('Rated 3.0', "RATED\n  Ambience is not that ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>
      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>
      <td>Addhuri Udupi Bhojana</td>
      <td>No</td>
      <td>No</td>
      <td>3.7/5</td>
      <td>88</td>
      <td>+91 9620009302</td>
      <td>Banashankari</td>
      <td>Quick Bites</td>
      <td>Masala Dosa</td>
      <td>South Indian, North Indian</td>
      <td>300</td>
      <td>[('Rated 4.0', "RATED\n  Great food and proper...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>Grand Village</td>
      <td>No</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>166</td>
      <td>+91 8026612447\r\n+91 9901210005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Panipuri, Gol Gappe</td>
      <td>North Indian, Rajasthani</td>
      <td>600</td>
      <td>[('Rated 4.0', 'RATED\n  Very good restaurant ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>100</th>
      <td>https://www.zomato.com/bangalore/kidambis-kitc...</td>
      <td>2465, 3rd Floor, Opposite BDA Complex, 24th Cr...</td>
      <td>Kidambi's Kitchen</td>
      <td>No</td>
      <td>No</td>
      <td>3.5/5</td>
      <td>52</td>
      <td>080 42112211\r\n+91 9880412211</td>
      <td>Banashankari</td>
      <td>Quick Bites</td>
      <td>Rooftop Ambience</td>
      <td>South Indian</td>
      <td>300</td>
      <td>[('Rated 4.0', 'RATED\n  If you are looking fo...</td>
      <td>[]</td>
      <td>Delivery</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>Grand Village</td>
      <td>No</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>166</td>
      <td>+91 8026612447\r\n+91 9901210005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Panipuri, Gol Gappe</td>
      <td>North Indian, Rajasthani</td>
      <td>600</td>
      <td>[('Rated 4.0', 'RATED\n  Very good restaurant ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>5</th>
      <td>https://www.zomato.com/bangalore/timepass-dinn...</td>
      <td>37, 5-1, 4th Floor, Bosco Court, Gandhi Bazaar...</td>
      <td>Timepass Dinner</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>286</td>
      <td>+91 9980040002\r\n+91 9980063005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Onion Rings, Pasta, Kadhai Paneer, Salads, Sal...</td>
      <td>North Indian</td>
      <td>600</td>
      <td>[('Rated 3.0', 'RATED\n  Food 3/5\nAmbience 3/...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>6</th>
      <td>https://www.zomato.com/bangalore/rosewood-inte...</td>
      <td>19/1, New Timberyard Layout, Beside Satellite ...</td>
      <td>Rosewood International Hotel - Bar &amp; Restaurant</td>
      <td>No</td>
      <td>No</td>
      <td>3.6/5</td>
      <td>8</td>
      <td>+91 9731716688\r\n080 26740366</td>
      <td>Mysore Road</td>
      <td>Casual Dining</td>
      <td>NaN</td>
      <td>North Indian, South Indian, Andhra, Chinese</td>
      <td>800</td>
      <td>[('Rated 5.0', 'RATED\n  Awesome food ??Great ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>Spice Elephant</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>San Churro Cafe</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>
      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>
      <td>Addhuri Udupi Bhojana</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>Grand Village</td>
    </tr>
    <tr>
      <th>5</th>
      <td>https://www.zomato.com/bangalore/timepass-dinn...</td>
      <td>37, 5-1, 4th Floor, Bosco Court, Gandhi Bazaar...</td>
      <td>Timepass Dinner</td>
    </tr>
    <tr>
      <th>6</th>
      <td>https://www.zomato.com/bangalore/rosewood-inte...</td>
      <td>19/1, New Timberyard Layout, Beside Satellite ...</td>
      <td>Rosewood International Hotel - Bar &amp; Restaurant</td>
    </tr>
    <tr>
      <th>7</th>
      <td>https://www.zomato.com/bangalore/onesta-banash...</td>
      <td>2469, 3rd Floor, 24th Cross, Opposite BDA Comp...</td>
      <td>Onesta</td>
    </tr>
    <tr>
      <th>8</th>
      <td>https://www.zomato.com/bangalore/penthouse-caf...</td>
      <td>1, 30th Main Road, 3rd Stage, Banashankari, Ba...</td>
      <td>Penthouse Cafe</td>
    </tr>
    <tr>
      <th>9</th>
      <td>https://www.zomato.com/bangalore/smacznego-ban...</td>
      <td>2470, 21 Main Road, 25th Cross, Banashankari, ...</td>
      <td>Smacznego</td>
    </tr>
  </tbody>
</table>
</div>



```python
display(ds1)
ds2 = ds1.fillna(value = 0 )
display(ds2)

```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Finocontrol Internship Selects (Off-Campus):</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>PwC India Associate (Consultant) Selects:</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>ZS Associates (Off-campus) - 2023 Batch</th>
      <th>...</th>
      <th>Unnamed: 27</th>
      <th>Unnamed: 28</th>
      <th>Unnamed: 29</th>
      <th>Unnamed: 30</th>
      <th>Unnamed: 31</th>
      <th>Unnamed: 32</th>
      <th>Unnamed: 33</th>
      <th>Unnamed: 34</th>
      <th>Unnamed: 35</th>
      <th>Unnamed: 36</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>. Ayush Dutta (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Gourab Nag (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1. H SANTOSH KUMAR (CIVIL)</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>. Ayush Dutta (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Finocontrol Internship Selects (Off-Campus):</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ankit Maurya (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Mainak Mondal (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2. KORIKANA SRI NIDHI (CIVIL)</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>Ankit Maurya (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Rushikesh Haribhau Dukare (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3. PRANSHU SINGHAL (CIVIL)</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3</td>
      <td>1. H SANTOSH KUMAR (CIVIL)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>ZS Associates (Off-campus) - 2023 Batch</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Varri Dileep Kumar (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4. RAJESH KUMAR JAISWAR (CIVIL)</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
      <td>2. KORIKANA SRI NIDHI (CIVIL)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>GOVINDA VINAY KUMAR (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5. RAJNISH KUMAR SUMAN (CIVIL)</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5</td>
      <td>3. PRANSHU SINGHAL (CIVIL)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Dheeravath Pranavika (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6. SHIVAM KUMAR (CIVIL)</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6</td>
      <td>4. RAJESH KUMAR JAISWAR (CIVIL)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Srujana Sarella (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7. N UMA TANMYEE ESHWARI (CIVIL)</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7</td>
      <td>5. RAJNISH KUMAR SUMAN (CIVIL)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>PRAHALAD DUTTA (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8. VIDUSHI GARG (CIVIL)</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>6. SHIVAM KUMAR (CIVIL)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Yaswanth Chakradhara Mahanti (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9</td>
      <td>7. N UMA TANMYEE ESHWARI (CIVIL)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>ASMITA DAS (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10</td>
      <td>8. VIDUSHI GARG (CIVIL)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Ritesh Kumar (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11</td>
      <td>Gourab Nag (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>PwC India Associate (Consultant) Selects:</td>
    </tr>
    <tr>
      <th>11</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>CHAITANYA KUMAR (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12</td>
      <td>Mainak Mondal (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13</td>
      <td>Rushikesh Haribhau Dukare (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14</td>
      <td>Varri Dileep Kumar (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15</td>
      <td>GOVINDA VINAY KUMAR (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>16</td>
      <td>Dheeravath Pranavika (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>17</td>
      <td>Srujana Sarella (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>18</td>
      <td>PRAHALAD DUTTA (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>19</td>
      <td>Yaswanth Chakradhara Mahanti (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20</td>
      <td>ASMITA DAS (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21</td>
      <td>Ritesh Kumar (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>22</td>
      <td>CHAITANYA KUMAR (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>23</td>
      <td>25) Akshat Tripathi (Civil)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Cognizant - Batch of 2023</td>
    </tr>
    <tr>
      <th>23</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24</td>
      <td>26) Debottam Saha (Civil)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>25</td>
      <td>27) DIPTIMAN DAS (Civil)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>26</td>
      <td>28) Prayas Pramanick (Civil)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>27</td>
      <td>29) Satyajit Giri (Civil)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28</td>
      <td>30) Shamik Roy (Civil)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>29</td>
      <td>31) Sridip Swapan Ganguly (Civil)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30</td>
      <td>32) Vikranth Kore (Civil)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>30</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>31</td>
      <td>Divyanshu(Civil)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Capgemini Senior Analyst</td>
    </tr>
    <tr>
      <th>31</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32</td>
      <td>1. Ipswita Das (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Accenture - Batch of 2023  Advance Application...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>33</td>
      <td>2. AYUSH DUTTA (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>34</td>
      <td>3. Anwesa Chakraborty (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35</td>
      <td>4. BHAVESH SONKAR (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36</td>
      <td>5. Ritwij Sen Sharma (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>36</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37</td>
      <td>6. NEEL DIGANTA BHADRA (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>38</td>
      <td>7. Prithviraj Deb Barman (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>39</td>
      <td>8. GOVINDA VINAY KUMAR (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>40</td>
      <td>9. Ritik Sagar (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>40</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41</td>
      <td>10. Astitva Singh (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>41</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>42</td>
      <td>11. ASMITA DAS (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>42</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>43</td>
      <td>. Shramana Chowdhury (CE)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>HSBC - Batch of 2023</td>
    </tr>
  </tbody>
</table>
<p>43 rows × 37 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Finocontrol Internship Selects (Off-Campus):</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>PwC India Associate (Consultant) Selects:</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>ZS Associates (Off-campus) - 2023 Batch</th>
      <th>...</th>
      <th>Unnamed: 27</th>
      <th>Unnamed: 28</th>
      <th>Unnamed: 29</th>
      <th>Unnamed: 30</th>
      <th>Unnamed: 31</th>
      <th>Unnamed: 32</th>
      <th>Unnamed: 33</th>
      <th>Unnamed: 34</th>
      <th>Unnamed: 35</th>
      <th>Unnamed: 36</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>. Ayush Dutta (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Gourab Nag (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1. H SANTOSH KUMAR (CIVIL)</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>. Ayush Dutta (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Finocontrol Internship Selects (Off-Campus):</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ankit Maurya (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Mainak Mondal (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2. KORIKANA SRI NIDHI (CIVIL)</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>Ankit Maurya (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Rushikesh Haribhau Dukare (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3. PRANSHU SINGHAL (CIVIL)</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3</td>
      <td>1. H SANTOSH KUMAR (CIVIL)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>ZS Associates (Off-campus) - 2023 Batch</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Varri Dileep Kumar (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4. RAJESH KUMAR JAISWAR (CIVIL)</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4</td>
      <td>2. KORIKANA SRI NIDHI (CIVIL)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>GOVINDA VINAY KUMAR (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5. RAJNISH KUMAR SUMAN (CIVIL)</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5</td>
      <td>3. PRANSHU SINGHAL (CIVIL)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Dheeravath Pranavika (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6. SHIVAM KUMAR (CIVIL)</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6</td>
      <td>4. RAJESH KUMAR JAISWAR (CIVIL)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Srujana Sarella (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7. N UMA TANMYEE ESHWARI (CIVIL)</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7</td>
      <td>5. RAJNISH KUMAR SUMAN (CIVIL)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>PRAHALAD DUTTA (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8. VIDUSHI GARG (CIVIL)</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8</td>
      <td>6. SHIVAM KUMAR (CIVIL)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Yaswanth Chakradhara Mahanti (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9</td>
      <td>7. N UMA TANMYEE ESHWARI (CIVIL)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>ASMITA DAS (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>10</td>
      <td>8. VIDUSHI GARG (CIVIL)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Ritesh Kumar (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>11</td>
      <td>Gourab Nag (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>PwC India Associate (Consultant) Selects:</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>CHAITANYA KUMAR (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>12</td>
      <td>Mainak Mondal (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>13</td>
      <td>Rushikesh Haribhau Dukare (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>14</td>
      <td>Varri Dileep Kumar (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15</td>
      <td>GOVINDA VINAY KUMAR (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>16</td>
      <td>Dheeravath Pranavika (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>17</td>
      <td>Srujana Sarella (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>18</td>
      <td>PRAHALAD DUTTA (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>19</td>
      <td>Yaswanth Chakradhara Mahanti (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>20</td>
      <td>ASMITA DAS (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>21</td>
      <td>Ritesh Kumar (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>22</td>
      <td>CHAITANYA KUMAR (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>23</td>
      <td>25) Akshat Tripathi (Civil)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Cognizant - Batch of 2023</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>24</td>
      <td>26) Debottam Saha (Civil)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>25</td>
      <td>27) DIPTIMAN DAS (Civil)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>26</td>
      <td>28) Prayas Pramanick (Civil)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>27</td>
      <td>29) Satyajit Giri (Civil)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>28</td>
      <td>30) Shamik Roy (Civil)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>29</td>
      <td>31) Sridip Swapan Ganguly (Civil)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>30</td>
      <td>32) Vikranth Kore (Civil)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>31</td>
      <td>Divyanshu(Civil)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Capgemini Senior Analyst</td>
    </tr>
    <tr>
      <th>31</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>32</td>
      <td>1. Ipswita Das (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Accenture - Batch of 2023  Advance Application...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>33</td>
      <td>2. AYUSH DUTTA (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>34</td>
      <td>3. Anwesa Chakraborty (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>34</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>35</td>
      <td>4. BHAVESH SONKAR (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>36</td>
      <td>5. Ritwij Sen Sharma (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>37</td>
      <td>6. NEEL DIGANTA BHADRA (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>38</td>
      <td>7. Prithviraj Deb Barman (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>39</td>
      <td>8. GOVINDA VINAY KUMAR (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>40</td>
      <td>9. Ritik Sagar (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>40</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>41</td>
      <td>10. Astitva Singh (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>42</td>
      <td>11. ASMITA DAS (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>42</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>43</td>
      <td>. Shramana Chowdhury (CE)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>HSBC - Batch of 2023</td>
    </tr>
  </tbody>
</table>
<p>43 rows × 37 columns</p>
</div>


<h3> describe() </h3>
<p> It is basically use for <strong>Numerical value </strong> in sheet. It descirbe below methods for every numerical column.   </p>


```python
ds1.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 10</th>
      <th>Unnamed: 11</th>
      <th>Unnamed: 12</th>
      <th>...</th>
      <th>Unnamed: 25</th>
      <th>Unnamed: 26</th>
      <th>Unnamed: 27</th>
      <th>Unnamed: 28</th>
      <th>Unnamed: 29</th>
      <th>Unnamed: 30</th>
      <th>Unnamed: 31</th>
      <th>Unnamed: 32</th>
      <th>Unnamed: 34</th>
      <th>Unnamed: 35</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>43.000000</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>22.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12.556539</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11.500000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>22.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32.500000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>43.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 28 columns</p>
</div>




```python
ds1.info() # it gives 
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 43 entries, 0 to 42
    Data columns (total 37 columns):
     #   Column                                        Non-Null Count  Dtype  
    ---  ------                                        --------------  -----  
     0   Finocontrol Internship Selects (Off-Campus):  2 non-null      object 
     1   Unnamed: 1                                    0 non-null      float64
     2   Unnamed: 2                                    0 non-null      float64
     3   Unnamed: 3                                    0 non-null      float64
     4   Unnamed: 4                                    0 non-null      float64
     5   PwC India Associate (Consultant) Selects:     12 non-null     object 
     6   Unnamed: 6                                    0 non-null      float64
     7   Unnamed: 7                                    0 non-null      float64
     8   Unnamed: 8                                    0 non-null      float64
     9   ZS Associates (Off-campus) - 2023 Batch       8 non-null      object 
     10  Unnamed: 10                                   0 non-null      float64
     11  Unnamed: 11                                   0 non-null      float64
     12  Unnamed: 12                                   0 non-null      float64
     13  Capgemini Senior Analyst                      1 non-null      object 
     14  Unnamed: 14                                   0 non-null      float64
     15  Unnamed: 15                                   0 non-null      float64
     16  Accenture - Batch of 2023                     12 non-null     object 
     17  Unnamed: 17                                   0 non-null      float64
     18  Unnamed: 18                                   0 non-null      float64
     19                                                0 non-null      float64
     20  HSBC - Batch of 2023                          1 non-null      object 
     21  Unnamed: 21                                   0 non-null      float64
     22  Unnamed: 22                                   0 non-null      float64
     23  Cognizant - Batch of 2023                     8 non-null      object 
     24  Unnamed: 24                                   0 non-null      float64
     25  Unnamed: 25                                   0 non-null      float64
     26  Unnamed: 26                                   0 non-null      float64
     27  Unnamed: 27                                   0 non-null      float64
     28  Unnamed: 28                                   0 non-null      float64
     29  Unnamed: 29                                   0 non-null      float64
     30  Unnamed: 30                                   0 non-null      float64
     31  Unnamed: 31                                   0 non-null      float64
     32  Unnamed: 32                                   43 non-null     int64  
     33  Unnamed: 33                                   43 non-null     object 
     34  Unnamed: 34                                   0 non-null      float64
     35  Unnamed: 35                                   0 non-null      float64
     36  Unnamed: 36                                   7 non-null      object 
    dtypes: float64(27), int64(1), object(9)
    memory usage: 12.6+ KB
    

Above RangeIndex is : Number of Rows
      Column is Number of Columns. 


```python
# It is used for get Name of the Columns in our sheets
ds1.columns
# ds1.rows is WRONG
```




    Index(['Finocontrol Internship Selects (Off-Campus):', 'Unnamed: 1',
           'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4',
           'PwC India Associate (Consultant) Selects:', 'Unnamed: 6', 'Unnamed: 7',
           'Unnamed: 8', 'ZS Associates (Off-campus) - 2023 Batch', 'Unnamed: 10',
           'Unnamed: 11', 'Unnamed: 12', 'Capgemini Senior Analyst', 'Unnamed: 14',
           'Unnamed: 15', 'Accenture - Batch of 2023', 'Unnamed: 17',
           'Unnamed: 18', ' ', 'HSBC - Batch of 2023', 'Unnamed: 21',
           'Unnamed: 22', 'Cognizant - Batch of 2023 ', 'Unnamed: 24',
           'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27', 'Unnamed: 28',
           'Unnamed: 29', 'Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32',
           'Unnamed: 33', 'Unnamed: 34', 'Unnamed: 35', 'Unnamed: 36'],
          dtype='object')



<div style = "display : flex; justify-content: center; ">
    <h1 style = "background-color: yellow; color:black; display:flex; padding:10px"> ds1['column_Name'].unique() </h1>
 </div>
 <h4> It gives unique Element of particular particular Column_Name <h4>


```python
a = ds1['Unnamed: 32'].unique()
arr = np.array(a)
```


```python
print(arr.size)
arr
```

    43
    




    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
           18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
           35, 36, 37, 38, 39, 40, 41, 42, 43], dtype=int64)



<div style = "display : flex; justify-content: center; ">
    <h1 style = "background-color: yellow; color:black; display:flex; padding:10px"> ds1['column_Name'].value_counts()</h1>
 </div>
 <h4> It gives Number of times the unique Element of particular  Column_Name have Occurs <h4>
    <p style = "font-family : The Times Roman"> For Example</p>


```python
valuecounts = ds1['Unnamed: 33'].value_counts()
```


```python
valuecounts
```




    . Ayush Dutta (CE)                   1
    2. AYUSH DUTTA (CE)                  1
    27) DIPTIMAN DAS (Civil)             1
    28) Prayas Pramanick (Civil)         1
    29) Satyajit Giri (Civil)            1
    30) Shamik Roy (Civil)               1
    31) Sridip Swapan Ganguly (Civil)    1
    32) Vikranth Kore (Civil)            1
    Divyanshu(Civil)                     1
    1. Ipswita Das (CE)                  1
    3. Anwesa Chakraborty (CE)           1
    25) Akshat Tripathi (Civil)          1
    4. BHAVESH SONKAR (CE)               1
    5. Ritwij Sen Sharma (CE)            1
    6. NEEL DIGANTA BHADRA (CE)          1
    7. Prithviraj Deb Barman (CE)        1
    8. GOVINDA VINAY KUMAR (CE)          1
    9. Ritik Sagar (CE)                  1
    10. Astitva Singh (CE)               1
    11. ASMITA DAS (CE)                  1
    26) Debottam Saha (Civil)            1
    CHAITANYA KUMAR (CE)                 1
    Ankit Maurya (CE)                    1
    Gourab Nag (CE)                      1
    1. H SANTOSH KUMAR (CIVIL)           1
    2. KORIKANA SRI NIDHI (CIVIL)        1
    3. PRANSHU SINGHAL (CIVIL)           1
    4. RAJESH KUMAR JAISWAR (CIVIL)      1
    5. RAJNISH KUMAR SUMAN (CIVIL)       1
    6. SHIVAM KUMAR (CIVIL)              1
    7. N UMA TANMYEE ESHWARI (CIVIL)     1
    8. VIDUSHI GARG (CIVIL)              1
    Mainak Mondal (CE)                   1
    Ritesh Kumar (CE)                    1
    Rushikesh Haribhau Dukare (CE)       1
    Varri Dileep Kumar (CE)              1
    GOVINDA VINAY KUMAR (CE)             1
    Dheeravath Pranavika (CE)            1
    Srujana Sarella (CE)                 1
    PRAHALAD DUTTA (CE)                  1
    Yaswanth Chakradhara Mahanti (CE)    1
    ASMITA DAS (CE)                      1
    . Shramana Chowdhury (CE)            1
    Name: Unnamed: 33, dtype: int64



<div style = "  display : flex; justify-content: center; ">
    <h1 style = " background-color: purple; color:white; display:flex; padding:10px"> DATA FRAME</h1>
 </div>
 

 <p style = "font-size : 17px ; ">A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, <br>or a table with rows and columns.</p >
 <p>For Example</p>


```python
import pandas as pd
data  = {
    'Names' : ['Vishal' , 'sneha' , 'souchit'],
    'BirthYear'  : [2000, 2001 , 2001]         
}
df3 = pd.DataFrame(data)
# df3.to_excel('small_df.xlsx')
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>BirthYear</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Vishal</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sneha</td>
      <td>2001</td>
    </tr>
    <tr>
      <th>2</th>
      <td>souchit</td>
      <td>2001</td>
    </tr>
  </tbody>
</table>
</div>



## Named Index

With the index argument, you can name your own indexes


```python
df3 = pd.DataFrame(data , index = ["Name1" , "Name2" , "Name3"])
display(df3)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>BirthYear</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Name1</th>
      <td>Vishal</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>Name2</th>
      <td>sneha</td>
      <td>2001</td>
    </tr>
    <tr>
      <th>Name3</th>
      <td>souchit</td>
      <td>2001</td>
    </tr>
  </tbody>
</table>
</div>


Refrence for DataFrame  :

https://www.w3schools.com/python/pandas/pandas_dataframes.asp

<div style = "  display : flex; justify-content: center; ">
    <h1 style = " background-color: purple; color:white; display:flex; padding:10px"> 
    Simple Filtering
    </h1>
 </div>


```python
series =df3['Names']
print("Type = ",type(series))
display(series)
```

    Type =  <class 'pandas.core.series.Series'>
    


    Name1     Vishal
    Name2      sneha
    Name3    souchit
    Name: Names, dtype: object



```python
# In DataFrame Type
display(df3[['Names']])
print("Type = " , type(df3[['Names']]))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Name1</th>
      <td>Vishal</td>
    </tr>
    <tr>
      <th>Name2</th>
      <td>sneha</td>
    </tr>
    <tr>
      <th>Name3</th>
      <td>souchit</td>
    </tr>
  </tbody>
</table>
</div>


    Type =  <class 'pandas.core.frame.DataFrame'>
    


```python
df3[df3['Names']=='Vishal']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>BirthYear</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Name1</th>
      <td>Vishal</td>
      <td>2000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4 = df3[df3['Names']=='Vishal']['BirthYear']
display(df4)
```


    Name1    2000
    Name: BirthYear, dtype: int64


<div style = "  display : flex; justify-content: center; ">
    <h1 style = " background-color: purple; color:white; display:flex; padding:10px"> 
    Complex Filtering With Zomato DataSet
    </h1>
 </div>


```python
# http://localhost:8888/edit/Jupyter_Python_learning/Pandas_HandsON/ExcelFile/zomato.csv
zm = pd.read_csv("ExcelFile/zomato.csv" )
```


```python

```


```python
OnlineOrder = zm[zm['online_order'] == 'Yes']   
OnlineOrder
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>Jalsa</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>Spice Elephant</td>
      <td>Yes</td>
      <td>No</td>
      <td>4.1/5</td>
      <td>787</td>
      <td>080 41714161</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>
      <td>Chinese, North Indian, Thai</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  Had been here for din...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>San Churro Cafe</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>918</td>
      <td>+91 9663487993</td>
      <td>Banashankari</td>
      <td>Cafe, Casual Dining</td>
      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>
      <td>Cafe, Mexican, Italian</td>
      <td>800</td>
      <td>[('Rated 3.0', "RATED\n  Ambience is not that ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>5</th>
      <td>https://www.zomato.com/bangalore/timepass-dinn...</td>
      <td>37, 5-1, 4th Floor, Bosco Court, Gandhi Bazaar...</td>
      <td>Timepass Dinner</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>286</td>
      <td>+91 9980040002\r\n+91 9980063005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Onion Rings, Pasta, Kadhai Paneer, Salads, Sal...</td>
      <td>North Indian</td>
      <td>600</td>
      <td>[('Rated 3.0', 'RATED\n  Food 3/5\nAmbience 3/...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>7</th>
      <td>https://www.zomato.com/bangalore/onesta-banash...</td>
      <td>2469, 3rd Floor, 24th Cross, Opposite BDA Comp...</td>
      <td>Onesta</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.6/5</td>
      <td>2556</td>
      <td>080 48653961\r\n080 48655715</td>
      <td>Banashankari</td>
      <td>Casual Dining, Cafe</td>
      <td>Farmhouse Pizza, Chocolate Banana, Virgin Moji...</td>
      <td>Pizza, Cafe, Italian</td>
      <td>600</td>
      <td>[('Rated 5.0', 'RATED\n  I personally really l...</td>
      <td>[]</td>
      <td>Cafes</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51697</th>
      <td>https://www.zomato.com/bangalore/shizusan-shop...</td>
      <td>Level 2, Phoenix Marketcity, Mahadevpura, Whit...</td>
      <td>Shizusan Shophouse &amp; Bar</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.4 /5</td>
      <td>1313</td>
      <td>080 67266655\n080 49626655</td>
      <td>Whitefield</td>
      <td>Casual Dining, Bar</td>
      <td>California Roll, Cocktails, Mocktails, Maki Ro...</td>
      <td>Asian, Japanese, Vietnamese, Korean, Chinese, ...</td>
      <td>1,800</td>
      <td>[('Rated 3.0', 'RATED\n  Wanted to try this pl...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51699</th>
      <td>https://www.zomato.com/bangalore/harrys-bar-ca...</td>
      <td>S-10, Level 2, Phoenix Market City, Whitefield...</td>
      <td>Harry's Bar + Cafe</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1 /5</td>
      <td>1218</td>
      <td>+91 7676924054\n+91 9137153744</td>
      <td>Whitefield</td>
      <td>Pub</td>
      <td>Cocktails, Beer, Long Island Iced Tea, Pasta, ...</td>
      <td>Asian, American, Mexican</td>
      <td>1,200</td>
      <td>[('Rated 4.0', 'RATED\n  The first thing that ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51701</th>
      <td>https://www.zomato.com/bangalore/the-beer-cafe...</td>
      <td>Unit 4A - 4B, Upper Ground Floor, VR Bengaluru...</td>
      <td>The Beer Cafe</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1 /5</td>
      <td>673</td>
      <td>+91 8929188573</td>
      <td>Whitefield</td>
      <td>Pub</td>
      <td>Cocktails, Wheat Beer, Bruschettas, Pasta, Bur...</td>
      <td>Finger Food, North Indian, Chinese, Italian</td>
      <td>1,400</td>
      <td>[('Rated 2.0', "RATED\n  We went out to this p...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51703</th>
      <td>https://www.zomato.com/bangalore/olivers-pub-d...</td>
      <td>ITPL Ascendas Park Square Mall, ITPL, First Fl...</td>
      <td>Oliver's Pub &amp; Diner</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>3.9 /5</td>
      <td>548</td>
      <td>+91 8043691111\n+91 8028026519</td>
      <td>Whitefield</td>
      <td>Pub, Casual Dining</td>
      <td>Pizza, Beer, Cocktails, Nachos, Pasta, Moo Bur...</td>
      <td>Finger Food, American, Continental, Burger, Pizza</td>
      <td>1,500</td>
      <td>[('Rated 4.0', "RATED\n  I had :-\n\n1. Italia...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51705</th>
      <td>https://www.zomato.com/bangalore/izakaya-gastr...</td>
      <td>2nd Floor, Iona, Virginia Mall, Whitefield Mai...</td>
      <td>Izakaya Gastro Pub</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>3.8 /5</td>
      <td>128</td>
      <td>+91 7625087121\n+91 8050587483</td>
      <td>Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>Beer, Chicken Guntur, Paneer Tikka, Fish, Nood...</td>
      <td>North Indian, Continental, Mediterranean</td>
      <td>1,200</td>
      <td>[('Rated 3.0', "RATED\n  Nice place to hangout...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
  </tbody>
</table>
<p>30444 rows × 17 columns</p>
</div>




```python
book_table = OnlineOrder[OnlineOrder['book_table'] == 'Yes']
book_table

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>Jalsa</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>7</th>
      <td>https://www.zomato.com/bangalore/onesta-banash...</td>
      <td>2469, 3rd Floor, 24th Cross, Opposite BDA Comp...</td>
      <td>Onesta</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.6/5</td>
      <td>2556</td>
      <td>080 48653961\r\n080 48655715</td>
      <td>Banashankari</td>
      <td>Casual Dining, Cafe</td>
      <td>Farmhouse Pizza, Chocolate Banana, Virgin Moji...</td>
      <td>Pizza, Cafe, Italian</td>
      <td>600</td>
      <td>[('Rated 5.0', 'RATED\n  I personally really l...</td>
      <td>[]</td>
      <td>Cafes</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>11</th>
      <td>https://www.zomato.com/bangalore/cafe-shuffle-...</td>
      <td>941, 3rd FLOOR, 21st Main, 22nd Cross, Banasha...</td>
      <td>Cafe Shuffle</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.2/5</td>
      <td>150</td>
      <td>+91 9742166777</td>
      <td>Banashankari</td>
      <td>Cafe</td>
      <td>Mocktails, Peri Fries, Lasagne, Pizza, Chicken...</td>
      <td>Cafe, Italian, Continental</td>
      <td>600</td>
      <td>[('Rated 1.0', "RATED\n \n\nHorrible. Not even...</td>
      <td>[]</td>
      <td>Cafes</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>12</th>
      <td>https://www.zomato.com/bangalore/the-coffee-sh...</td>
      <td>6th Block, 3rd Stage, Banashankari, Bangalore</td>
      <td>The Coffee Shack</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.2/5</td>
      <td>164</td>
      <td>+91 9731644212</td>
      <td>Banashankari</td>
      <td>Cafe</td>
      <td>Coffee, Spaghetti, Pancakes, Nachos, Pasta, Sa...</td>
      <td>Cafe, Chinese, Continental, Italian</td>
      <td>500</td>
      <td>[('Rated 4.0', "RATED\n  Food - 4/5\nAmbience ...</td>
      <td>[]</td>
      <td>Cafes</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>44</th>
      <td>https://www.zomato.com/bangalore/onesta-banash...</td>
      <td>2469, 3rd Floor, 24th Cross, Opposite BDA Comp...</td>
      <td>Onesta</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.6/5</td>
      <td>2556</td>
      <td>080 48653961\r\n080 48655715</td>
      <td>Banashankari</td>
      <td>Casual Dining, Cafe</td>
      <td>Farmhouse Pizza, Chocolate Banana, Virgin Moji...</td>
      <td>Pizza, Cafe, Italian</td>
      <td>600</td>
      <td>[('Rated 5.0', 'RATED\n  I personally really l...</td>
      <td>[]</td>
      <td>Delivery</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51697</th>
      <td>https://www.zomato.com/bangalore/shizusan-shop...</td>
      <td>Level 2, Phoenix Marketcity, Mahadevpura, Whit...</td>
      <td>Shizusan Shophouse &amp; Bar</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.4 /5</td>
      <td>1313</td>
      <td>080 67266655\n080 49626655</td>
      <td>Whitefield</td>
      <td>Casual Dining, Bar</td>
      <td>California Roll, Cocktails, Mocktails, Maki Ro...</td>
      <td>Asian, Japanese, Vietnamese, Korean, Chinese, ...</td>
      <td>1,800</td>
      <td>[('Rated 3.0', 'RATED\n  Wanted to try this pl...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51699</th>
      <td>https://www.zomato.com/bangalore/harrys-bar-ca...</td>
      <td>S-10, Level 2, Phoenix Market City, Whitefield...</td>
      <td>Harry's Bar + Cafe</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1 /5</td>
      <td>1218</td>
      <td>+91 7676924054\n+91 9137153744</td>
      <td>Whitefield</td>
      <td>Pub</td>
      <td>Cocktails, Beer, Long Island Iced Tea, Pasta, ...</td>
      <td>Asian, American, Mexican</td>
      <td>1,200</td>
      <td>[('Rated 4.0', 'RATED\n  The first thing that ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51701</th>
      <td>https://www.zomato.com/bangalore/the-beer-cafe...</td>
      <td>Unit 4A - 4B, Upper Ground Floor, VR Bengaluru...</td>
      <td>The Beer Cafe</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1 /5</td>
      <td>673</td>
      <td>+91 8929188573</td>
      <td>Whitefield</td>
      <td>Pub</td>
      <td>Cocktails, Wheat Beer, Bruschettas, Pasta, Bur...</td>
      <td>Finger Food, North Indian, Chinese, Italian</td>
      <td>1,400</td>
      <td>[('Rated 2.0', "RATED\n  We went out to this p...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51703</th>
      <td>https://www.zomato.com/bangalore/olivers-pub-d...</td>
      <td>ITPL Ascendas Park Square Mall, ITPL, First Fl...</td>
      <td>Oliver's Pub &amp; Diner</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>3.9 /5</td>
      <td>548</td>
      <td>+91 8043691111\n+91 8028026519</td>
      <td>Whitefield</td>
      <td>Pub, Casual Dining</td>
      <td>Pizza, Beer, Cocktails, Nachos, Pasta, Moo Bur...</td>
      <td>Finger Food, American, Continental, Burger, Pizza</td>
      <td>1,500</td>
      <td>[('Rated 4.0', "RATED\n  I had :-\n\n1. Italia...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51705</th>
      <td>https://www.zomato.com/bangalore/izakaya-gastr...</td>
      <td>2nd Floor, Iona, Virginia Mall, Whitefield Mai...</td>
      <td>Izakaya Gastro Pub</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>3.8 /5</td>
      <td>128</td>
      <td>+91 7625087121\n+91 8050587483</td>
      <td>Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>Beer, Chicken Guntur, Paneer Tikka, Fish, Nood...</td>
      <td>North Indian, Continental, Mediterranean</td>
      <td>1,200</td>
      <td>[('Rated 3.0', "RATED\n  Nice place to hangout...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
  </tbody>
</table>
<p>3805 rows × 17 columns</p>
</div>




```python
print(book_table.shape)
# There is another way to write the above complex filtering in one line 
zm[(zm['online_order'] == 'Yes') & (zm['book_table'] == 'Yes')]
```

    (3805, 17)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>Jalsa</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>7</th>
      <td>https://www.zomato.com/bangalore/onesta-banash...</td>
      <td>2469, 3rd Floor, 24th Cross, Opposite BDA Comp...</td>
      <td>Onesta</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.6/5</td>
      <td>2556</td>
      <td>080 48653961\r\n080 48655715</td>
      <td>Banashankari</td>
      <td>Casual Dining, Cafe</td>
      <td>Farmhouse Pizza, Chocolate Banana, Virgin Moji...</td>
      <td>Pizza, Cafe, Italian</td>
      <td>600</td>
      <td>[('Rated 5.0', 'RATED\n  I personally really l...</td>
      <td>[]</td>
      <td>Cafes</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>11</th>
      <td>https://www.zomato.com/bangalore/cafe-shuffle-...</td>
      <td>941, 3rd FLOOR, 21st Main, 22nd Cross, Banasha...</td>
      <td>Cafe Shuffle</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.2/5</td>
      <td>150</td>
      <td>+91 9742166777</td>
      <td>Banashankari</td>
      <td>Cafe</td>
      <td>Mocktails, Peri Fries, Lasagne, Pizza, Chicken...</td>
      <td>Cafe, Italian, Continental</td>
      <td>600</td>
      <td>[('Rated 1.0', "RATED\n \n\nHorrible. Not even...</td>
      <td>[]</td>
      <td>Cafes</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>12</th>
      <td>https://www.zomato.com/bangalore/the-coffee-sh...</td>
      <td>6th Block, 3rd Stage, Banashankari, Bangalore</td>
      <td>The Coffee Shack</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.2/5</td>
      <td>164</td>
      <td>+91 9731644212</td>
      <td>Banashankari</td>
      <td>Cafe</td>
      <td>Coffee, Spaghetti, Pancakes, Nachos, Pasta, Sa...</td>
      <td>Cafe, Chinese, Continental, Italian</td>
      <td>500</td>
      <td>[('Rated 4.0', "RATED\n  Food - 4/5\nAmbience ...</td>
      <td>[]</td>
      <td>Cafes</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>44</th>
      <td>https://www.zomato.com/bangalore/onesta-banash...</td>
      <td>2469, 3rd Floor, 24th Cross, Opposite BDA Comp...</td>
      <td>Onesta</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.6/5</td>
      <td>2556</td>
      <td>080 48653961\r\n080 48655715</td>
      <td>Banashankari</td>
      <td>Casual Dining, Cafe</td>
      <td>Farmhouse Pizza, Chocolate Banana, Virgin Moji...</td>
      <td>Pizza, Cafe, Italian</td>
      <td>600</td>
      <td>[('Rated 5.0', 'RATED\n  I personally really l...</td>
      <td>[]</td>
      <td>Delivery</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51697</th>
      <td>https://www.zomato.com/bangalore/shizusan-shop...</td>
      <td>Level 2, Phoenix Marketcity, Mahadevpura, Whit...</td>
      <td>Shizusan Shophouse &amp; Bar</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.4 /5</td>
      <td>1313</td>
      <td>080 67266655\n080 49626655</td>
      <td>Whitefield</td>
      <td>Casual Dining, Bar</td>
      <td>California Roll, Cocktails, Mocktails, Maki Ro...</td>
      <td>Asian, Japanese, Vietnamese, Korean, Chinese, ...</td>
      <td>1,800</td>
      <td>[('Rated 3.0', 'RATED\n  Wanted to try this pl...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51699</th>
      <td>https://www.zomato.com/bangalore/harrys-bar-ca...</td>
      <td>S-10, Level 2, Phoenix Market City, Whitefield...</td>
      <td>Harry's Bar + Cafe</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1 /5</td>
      <td>1218</td>
      <td>+91 7676924054\n+91 9137153744</td>
      <td>Whitefield</td>
      <td>Pub</td>
      <td>Cocktails, Beer, Long Island Iced Tea, Pasta, ...</td>
      <td>Asian, American, Mexican</td>
      <td>1,200</td>
      <td>[('Rated 4.0', 'RATED\n  The first thing that ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51701</th>
      <td>https://www.zomato.com/bangalore/the-beer-cafe...</td>
      <td>Unit 4A - 4B, Upper Ground Floor, VR Bengaluru...</td>
      <td>The Beer Cafe</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1 /5</td>
      <td>673</td>
      <td>+91 8929188573</td>
      <td>Whitefield</td>
      <td>Pub</td>
      <td>Cocktails, Wheat Beer, Bruschettas, Pasta, Bur...</td>
      <td>Finger Food, North Indian, Chinese, Italian</td>
      <td>1,400</td>
      <td>[('Rated 2.0', "RATED\n  We went out to this p...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51703</th>
      <td>https://www.zomato.com/bangalore/olivers-pub-d...</td>
      <td>ITPL Ascendas Park Square Mall, ITPL, First Fl...</td>
      <td>Oliver's Pub &amp; Diner</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>3.9 /5</td>
      <td>548</td>
      <td>+91 8043691111\n+91 8028026519</td>
      <td>Whitefield</td>
      <td>Pub, Casual Dining</td>
      <td>Pizza, Beer, Cocktails, Nachos, Pasta, Moo Bur...</td>
      <td>Finger Food, American, Continental, Burger, Pizza</td>
      <td>1,500</td>
      <td>[('Rated 4.0', "RATED\n  I had :-\n\n1. Italia...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51705</th>
      <td>https://www.zomato.com/bangalore/izakaya-gastr...</td>
      <td>2nd Floor, Iona, Virginia Mall, Whitefield Mai...</td>
      <td>Izakaya Gastro Pub</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>3.8 /5</td>
      <td>128</td>
      <td>+91 7625087121\n+91 8050587483</td>
      <td>Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>Beer, Chicken Guntur, Paneer Tikka, Fish, Nood...</td>
      <td>North Indian, Continental, Mediterranean</td>
      <td>1,200</td>
      <td>[('Rated 3.0', "RATED\n  Nice place to hangout...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
  </tbody>
</table>
<p>3805 rows × 17 columns</p>
</div>



<div style = "  display : flex; justify-content: center; ">
    <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
    Add and Remove Columns 
    </h1>
   
 </div>
  <p> <br> To get Add Column  <b> zm['Column_Name'] = 'Column_Value' 
    </b> //--> this will to give all the rows same value </p>


```python
zm['Column_Name'] = 'Column_Value'
zm
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
      <th>Column_Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>Jalsa</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>Spice Elephant</td>
      <td>Yes</td>
      <td>No</td>
      <td>4.1/5</td>
      <td>787</td>
      <td>080 41714161</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>
      <td>Chinese, North Indian, Thai</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  Had been here for din...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>San Churro Cafe</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>918</td>
      <td>+91 9663487993</td>
      <td>Banashankari</td>
      <td>Cafe, Casual Dining</td>
      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>
      <td>Cafe, Mexican, Italian</td>
      <td>800</td>
      <td>[('Rated 3.0', "RATED\n  Ambience is not that ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>
      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>
      <td>Addhuri Udupi Bhojana</td>
      <td>No</td>
      <td>No</td>
      <td>3.7/5</td>
      <td>88</td>
      <td>+91 9620009302</td>
      <td>Banashankari</td>
      <td>Quick Bites</td>
      <td>Masala Dosa</td>
      <td>South Indian, North Indian</td>
      <td>300</td>
      <td>[('Rated 4.0', "RATED\n  Great food and proper...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>Grand Village</td>
      <td>No</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>166</td>
      <td>+91 8026612447\r\n+91 9901210005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Panipuri, Gol Gappe</td>
      <td>North Indian, Rajasthani</td>
      <td>600</td>
      <td>[('Rated 4.0', 'RATED\n  Very good restaurant ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51712</th>
      <td>https://www.zomato.com/bangalore/best-brews-fo...</td>
      <td>Four Points by Sheraton Bengaluru, 43/3, White...</td>
      <td>Best Brews - Four Points by Sheraton Bengaluru...</td>
      <td>No</td>
      <td>No</td>
      <td>3.6 /5</td>
      <td>27</td>
      <td>080 40301477</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', "RATED\n  Food and service are ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51713</th>
      <td>https://www.zomato.com/bangalore/vinod-bar-and...</td>
      <td>Number 10, Garudachar Palya, Mahadevapura, Whi...</td>
      <td>Vinod Bar And Restaurant</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>+91 8197675843</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>600</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51714</th>
      <td>https://www.zomato.com/bangalore/plunge-sherat...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Plunge - Sheraton Grand Bengaluru Whitefield H...</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>2,000</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51715</th>
      <td>https://www.zomato.com/bangalore/chime-sherato...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Chime - Sheraton Grand Bengaluru Whitefield Ho...</td>
      <td>No</td>
      <td>Yes</td>
      <td>4.3 /5</td>
      <td>236</td>
      <td>080 49652769</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar</td>
      <td>Cocktails, Pizza, Buttermilk</td>
      <td>Finger Food</td>
      <td>2,500</td>
      <td>[('Rated 4.0', 'RATED\n  Nice and friendly pla...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51716</th>
      <td>https://www.zomato.com/bangalore/the-nest-the-...</td>
      <td>ITPL Main Road, KIADB Export Promotion Industr...</td>
      <td>The Nest - The Den Bengaluru</td>
      <td>No</td>
      <td>No</td>
      <td>3.4 /5</td>
      <td>13</td>
      <td>+91 8071117272</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>NaN</td>
      <td>Finger Food, North Indian, Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', 'RATED\n  Great ambience , look...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
  </tbody>
</table>
<p>51717 rows × 18 columns</p>
</div>



![image.png](attachment:image.png)

## To Remove (zm.drop)


```python
# Axis = 1 means Column wise
#  Axis = 0 menas row wise
zm.drop('Column_Name' , axis = 1)
# Here it is Not permanently Deleted. If you again print 'zm'.
# To Delete permanently we have to use "inplace" or
# '''  We can do
# zm = zm.drop('Column_Name' , axis = 1)  # This is over writing in exsisting variable
#         OR(use inplace)
# zm.drop('Column_Name' ,axis=1, inplace ="true")        
# '''
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>Jalsa</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>Spice Elephant</td>
      <td>Yes</td>
      <td>No</td>
      <td>4.1/5</td>
      <td>787</td>
      <td>080 41714161</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>
      <td>Chinese, North Indian, Thai</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  Had been here for din...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>San Churro Cafe</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>918</td>
      <td>+91 9663487993</td>
      <td>Banashankari</td>
      <td>Cafe, Casual Dining</td>
      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>
      <td>Cafe, Mexican, Italian</td>
      <td>800</td>
      <td>[('Rated 3.0', "RATED\n  Ambience is not that ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>
      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>
      <td>Addhuri Udupi Bhojana</td>
      <td>No</td>
      <td>No</td>
      <td>3.7/5</td>
      <td>88</td>
      <td>+91 9620009302</td>
      <td>Banashankari</td>
      <td>Quick Bites</td>
      <td>Masala Dosa</td>
      <td>South Indian, North Indian</td>
      <td>300</td>
      <td>[('Rated 4.0', "RATED\n  Great food and proper...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>Grand Village</td>
      <td>No</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>166</td>
      <td>+91 8026612447\r\n+91 9901210005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Panipuri, Gol Gappe</td>
      <td>North Indian, Rajasthani</td>
      <td>600</td>
      <td>[('Rated 4.0', 'RATED\n  Very good restaurant ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51712</th>
      <td>https://www.zomato.com/bangalore/best-brews-fo...</td>
      <td>Four Points by Sheraton Bengaluru, 43/3, White...</td>
      <td>Best Brews - Four Points by Sheraton Bengaluru...</td>
      <td>No</td>
      <td>No</td>
      <td>3.6 /5</td>
      <td>27</td>
      <td>080 40301477</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', "RATED\n  Food and service are ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51713</th>
      <td>https://www.zomato.com/bangalore/vinod-bar-and...</td>
      <td>Number 10, Garudachar Palya, Mahadevapura, Whi...</td>
      <td>Vinod Bar And Restaurant</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>+91 8197675843</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>600</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51714</th>
      <td>https://www.zomato.com/bangalore/plunge-sherat...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Plunge - Sheraton Grand Bengaluru Whitefield H...</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>2,000</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51715</th>
      <td>https://www.zomato.com/bangalore/chime-sherato...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Chime - Sheraton Grand Bengaluru Whitefield Ho...</td>
      <td>No</td>
      <td>Yes</td>
      <td>4.3 /5</td>
      <td>236</td>
      <td>080 49652769</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar</td>
      <td>Cocktails, Pizza, Buttermilk</td>
      <td>Finger Food</td>
      <td>2,500</td>
      <td>[('Rated 4.0', 'RATED\n  Nice and friendly pla...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51716</th>
      <td>https://www.zomato.com/bangalore/the-nest-the-...</td>
      <td>ITPL Main Road, KIADB Export Promotion Industr...</td>
      <td>The Nest - The Den Bengaluru</td>
      <td>No</td>
      <td>No</td>
      <td>3.4 /5</td>
      <td>13</td>
      <td>+91 8071117272</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>NaN</td>
      <td>Finger Food, North Indian, Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', 'RATED\n  Great ambience , look...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
  </tbody>
</table>
<p>51717 rows × 17 columns</p>
</div>




```python
zm
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
      <th>Column_Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>Jalsa</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>Spice Elephant</td>
      <td>Yes</td>
      <td>No</td>
      <td>4.1/5</td>
      <td>787</td>
      <td>080 41714161</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>
      <td>Chinese, North Indian, Thai</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  Had been here for din...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>San Churro Cafe</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>918</td>
      <td>+91 9663487993</td>
      <td>Banashankari</td>
      <td>Cafe, Casual Dining</td>
      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>
      <td>Cafe, Mexican, Italian</td>
      <td>800</td>
      <td>[('Rated 3.0', "RATED\n  Ambience is not that ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>
      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>
      <td>Addhuri Udupi Bhojana</td>
      <td>No</td>
      <td>No</td>
      <td>3.7/5</td>
      <td>88</td>
      <td>+91 9620009302</td>
      <td>Banashankari</td>
      <td>Quick Bites</td>
      <td>Masala Dosa</td>
      <td>South Indian, North Indian</td>
      <td>300</td>
      <td>[('Rated 4.0', "RATED\n  Great food and proper...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>Grand Village</td>
      <td>No</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>166</td>
      <td>+91 8026612447\r\n+91 9901210005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Panipuri, Gol Gappe</td>
      <td>North Indian, Rajasthani</td>
      <td>600</td>
      <td>[('Rated 4.0', 'RATED\n  Very good restaurant ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51712</th>
      <td>https://www.zomato.com/bangalore/best-brews-fo...</td>
      <td>Four Points by Sheraton Bengaluru, 43/3, White...</td>
      <td>Best Brews - Four Points by Sheraton Bengaluru...</td>
      <td>No</td>
      <td>No</td>
      <td>3.6 /5</td>
      <td>27</td>
      <td>080 40301477</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', "RATED\n  Food and service are ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51713</th>
      <td>https://www.zomato.com/bangalore/vinod-bar-and...</td>
      <td>Number 10, Garudachar Palya, Mahadevapura, Whi...</td>
      <td>Vinod Bar And Restaurant</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>+91 8197675843</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>600</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51714</th>
      <td>https://www.zomato.com/bangalore/plunge-sherat...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Plunge - Sheraton Grand Bengaluru Whitefield H...</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>2,000</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51715</th>
      <td>https://www.zomato.com/bangalore/chime-sherato...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Chime - Sheraton Grand Bengaluru Whitefield Ho...</td>
      <td>No</td>
      <td>Yes</td>
      <td>4.3 /5</td>
      <td>236</td>
      <td>080 49652769</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar</td>
      <td>Cocktails, Pizza, Buttermilk</td>
      <td>Finger Food</td>
      <td>2,500</td>
      <td>[('Rated 4.0', 'RATED\n  Nice and friendly pla...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51716</th>
      <td>https://www.zomato.com/bangalore/the-nest-the-...</td>
      <td>ITPL Main Road, KIADB Export Promotion Industr...</td>
      <td>The Nest - The Den Bengaluru</td>
      <td>No</td>
      <td>No</td>
      <td>3.4 /5</td>
      <td>13</td>
      <td>+91 8071117272</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>NaN</td>
      <td>Finger Food, North Indian, Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', 'RATED\n  Great ambience , look...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
  </tbody>
</table>
<p>51717 rows × 18 columns</p>
</div>




```python
zm
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
      <th>Column_Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>Jalsa</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>Spice Elephant</td>
      <td>Yes</td>
      <td>No</td>
      <td>4.1/5</td>
      <td>787</td>
      <td>080 41714161</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>
      <td>Chinese, North Indian, Thai</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  Had been here for din...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>San Churro Cafe</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>918</td>
      <td>+91 9663487993</td>
      <td>Banashankari</td>
      <td>Cafe, Casual Dining</td>
      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>
      <td>Cafe, Mexican, Italian</td>
      <td>800</td>
      <td>[('Rated 3.0', "RATED\n  Ambience is not that ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>
      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>
      <td>Addhuri Udupi Bhojana</td>
      <td>No</td>
      <td>No</td>
      <td>3.7/5</td>
      <td>88</td>
      <td>+91 9620009302</td>
      <td>Banashankari</td>
      <td>Quick Bites</td>
      <td>Masala Dosa</td>
      <td>South Indian, North Indian</td>
      <td>300</td>
      <td>[('Rated 4.0', "RATED\n  Great food and proper...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>Grand Village</td>
      <td>No</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>166</td>
      <td>+91 8026612447\r\n+91 9901210005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Panipuri, Gol Gappe</td>
      <td>North Indian, Rajasthani</td>
      <td>600</td>
      <td>[('Rated 4.0', 'RATED\n  Very good restaurant ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51712</th>
      <td>https://www.zomato.com/bangalore/best-brews-fo...</td>
      <td>Four Points by Sheraton Bengaluru, 43/3, White...</td>
      <td>Best Brews - Four Points by Sheraton Bengaluru...</td>
      <td>No</td>
      <td>No</td>
      <td>3.6 /5</td>
      <td>27</td>
      <td>080 40301477</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', "RATED\n  Food and service are ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51713</th>
      <td>https://www.zomato.com/bangalore/vinod-bar-and...</td>
      <td>Number 10, Garudachar Palya, Mahadevapura, Whi...</td>
      <td>Vinod Bar And Restaurant</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>+91 8197675843</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>600</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51714</th>
      <td>https://www.zomato.com/bangalore/plunge-sherat...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Plunge - Sheraton Grand Bengaluru Whitefield H...</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>2,000</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51715</th>
      <td>https://www.zomato.com/bangalore/chime-sherato...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Chime - Sheraton Grand Bengaluru Whitefield Ho...</td>
      <td>No</td>
      <td>Yes</td>
      <td>4.3 /5</td>
      <td>236</td>
      <td>080 49652769</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar</td>
      <td>Cocktails, Pizza, Buttermilk</td>
      <td>Finger Food</td>
      <td>2,500</td>
      <td>[('Rated 4.0', 'RATED\n  Nice and friendly pla...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
    <tr>
      <th>51716</th>
      <td>https://www.zomato.com/bangalore/the-nest-the-...</td>
      <td>ITPL Main Road, KIADB Export Promotion Industr...</td>
      <td>The Nest - The Den Bengaluru</td>
      <td>No</td>
      <td>No</td>
      <td>3.4 /5</td>
      <td>13</td>
      <td>+91 8071117272</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>NaN</td>
      <td>Finger Food, North Indian, Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', 'RATED\n  Great ambience , look...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_Value</td>
    </tr>
  </tbody>
</table>
<p>51717 rows × 18 columns</p>
</div>




```python
zm.drop('Column_Name', axis=1, inplace = True)
zm
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>Jalsa</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>Spice Elephant</td>
      <td>Yes</td>
      <td>No</td>
      <td>4.1/5</td>
      <td>787</td>
      <td>080 41714161</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>
      <td>Chinese, North Indian, Thai</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  Had been here for din...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>San Churro Cafe</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>918</td>
      <td>+91 9663487993</td>
      <td>Banashankari</td>
      <td>Cafe, Casual Dining</td>
      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>
      <td>Cafe, Mexican, Italian</td>
      <td>800</td>
      <td>[('Rated 3.0', "RATED\n  Ambience is not that ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>
      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>
      <td>Addhuri Udupi Bhojana</td>
      <td>No</td>
      <td>No</td>
      <td>3.7/5</td>
      <td>88</td>
      <td>+91 9620009302</td>
      <td>Banashankari</td>
      <td>Quick Bites</td>
      <td>Masala Dosa</td>
      <td>South Indian, North Indian</td>
      <td>300</td>
      <td>[('Rated 4.0', "RATED\n  Great food and proper...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>Grand Village</td>
      <td>No</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>166</td>
      <td>+91 8026612447\r\n+91 9901210005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Panipuri, Gol Gappe</td>
      <td>North Indian, Rajasthani</td>
      <td>600</td>
      <td>[('Rated 4.0', 'RATED\n  Very good restaurant ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51712</th>
      <td>https://www.zomato.com/bangalore/best-brews-fo...</td>
      <td>Four Points by Sheraton Bengaluru, 43/3, White...</td>
      <td>Best Brews - Four Points by Sheraton Bengaluru...</td>
      <td>No</td>
      <td>No</td>
      <td>3.6 /5</td>
      <td>27</td>
      <td>080 40301477</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', "RATED\n  Food and service are ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51713</th>
      <td>https://www.zomato.com/bangalore/vinod-bar-and...</td>
      <td>Number 10, Garudachar Palya, Mahadevapura, Whi...</td>
      <td>Vinod Bar And Restaurant</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>+91 8197675843</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>600</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51714</th>
      <td>https://www.zomato.com/bangalore/plunge-sherat...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Plunge - Sheraton Grand Bengaluru Whitefield H...</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>2,000</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51715</th>
      <td>https://www.zomato.com/bangalore/chime-sherato...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Chime - Sheraton Grand Bengaluru Whitefield Ho...</td>
      <td>No</td>
      <td>Yes</td>
      <td>4.3 /5</td>
      <td>236</td>
      <td>080 49652769</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar</td>
      <td>Cocktails, Pizza, Buttermilk</td>
      <td>Finger Food</td>
      <td>2,500</td>
      <td>[('Rated 4.0', 'RATED\n  Nice and friendly pla...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51716</th>
      <td>https://www.zomato.com/bangalore/the-nest-the-...</td>
      <td>ITPL Main Road, KIADB Export Promotion Industr...</td>
      <td>The Nest - The Den Bengaluru</td>
      <td>No</td>
      <td>No</td>
      <td>3.4 /5</td>
      <td>13</td>
      <td>+91 8071117272</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>NaN</td>
      <td>Finger Food, North Indian, Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', 'RATED\n  Great ambience , look...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
  </tbody>
</table>
<p>51717 rows × 17 columns</p>
</div>




```python
zm

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>Jalsa</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>Spice Elephant</td>
      <td>Yes</td>
      <td>No</td>
      <td>4.1/5</td>
      <td>787</td>
      <td>080 41714161</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>
      <td>Chinese, North Indian, Thai</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  Had been here for din...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>San Churro Cafe</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>918</td>
      <td>+91 9663487993</td>
      <td>Banashankari</td>
      <td>Cafe, Casual Dining</td>
      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>
      <td>Cafe, Mexican, Italian</td>
      <td>800</td>
      <td>[('Rated 3.0', "RATED\n  Ambience is not that ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>
      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>
      <td>Addhuri Udupi Bhojana</td>
      <td>No</td>
      <td>No</td>
      <td>3.7/5</td>
      <td>88</td>
      <td>+91 9620009302</td>
      <td>Banashankari</td>
      <td>Quick Bites</td>
      <td>Masala Dosa</td>
      <td>South Indian, North Indian</td>
      <td>300</td>
      <td>[('Rated 4.0', "RATED\n  Great food and proper...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>Grand Village</td>
      <td>No</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>166</td>
      <td>+91 8026612447\r\n+91 9901210005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Panipuri, Gol Gappe</td>
      <td>North Indian, Rajasthani</td>
      <td>600</td>
      <td>[('Rated 4.0', 'RATED\n  Very good restaurant ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51712</th>
      <td>https://www.zomato.com/bangalore/best-brews-fo...</td>
      <td>Four Points by Sheraton Bengaluru, 43/3, White...</td>
      <td>Best Brews - Four Points by Sheraton Bengaluru...</td>
      <td>No</td>
      <td>No</td>
      <td>3.6 /5</td>
      <td>27</td>
      <td>080 40301477</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', "RATED\n  Food and service are ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51713</th>
      <td>https://www.zomato.com/bangalore/vinod-bar-and...</td>
      <td>Number 10, Garudachar Palya, Mahadevapura, Whi...</td>
      <td>Vinod Bar And Restaurant</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>+91 8197675843</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>600</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51714</th>
      <td>https://www.zomato.com/bangalore/plunge-sherat...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Plunge - Sheraton Grand Bengaluru Whitefield H...</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>2,000</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51715</th>
      <td>https://www.zomato.com/bangalore/chime-sherato...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Chime - Sheraton Grand Bengaluru Whitefield Ho...</td>
      <td>No</td>
      <td>Yes</td>
      <td>4.3 /5</td>
      <td>236</td>
      <td>080 49652769</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar</td>
      <td>Cocktails, Pizza, Buttermilk</td>
      <td>Finger Food</td>
      <td>2,500</td>
      <td>[('Rated 4.0', 'RATED\n  Nice and friendly pla...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
    <tr>
      <th>51716</th>
      <td>https://www.zomato.com/bangalore/the-nest-the-...</td>
      <td>ITPL Main Road, KIADB Export Promotion Industr...</td>
      <td>The Nest - The Den Bengaluru</td>
      <td>No</td>
      <td>No</td>
      <td>3.4 /5</td>
      <td>13</td>
      <td>+91 8071117272</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>NaN</td>
      <td>Finger Food, North Indian, Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', 'RATED\n  Great ambience , look...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
    </tr>
  </tbody>
</table>
<p>51717 rows × 17 columns</p>
</div>



<div style = "  display : flex; justify-content: center; ">
    <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
    Renaming And Reordering 
    </h1>
   
 </div>
  <p> <br>  </p>

## Rename
Lets I want to rename Column_Name to Values
.rename()   function 

Example


```python
zm['Column_Name'] = 'Column_value'
```


```python

```


```python

#  to change it permanent 
zm.rename(columns = {
         'Column_Name' : 'Values'} , inplace = True )
```


```python
zm
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>address</th>
      <th>name</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
      <th>Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>Jalsa</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_value</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>Spice Elephant</td>
      <td>Yes</td>
      <td>No</td>
      <td>4.1/5</td>
      <td>787</td>
      <td>080 41714161</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>
      <td>Chinese, North Indian, Thai</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  Had been here for din...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_value</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>San Churro Cafe</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>918</td>
      <td>+91 9663487993</td>
      <td>Banashankari</td>
      <td>Cafe, Casual Dining</td>
      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>
      <td>Cafe, Mexican, Italian</td>
      <td>800</td>
      <td>[('Rated 3.0', "RATED\n  Ambience is not that ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_value</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>
      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>
      <td>Addhuri Udupi Bhojana</td>
      <td>No</td>
      <td>No</td>
      <td>3.7/5</td>
      <td>88</td>
      <td>+91 9620009302</td>
      <td>Banashankari</td>
      <td>Quick Bites</td>
      <td>Masala Dosa</td>
      <td>South Indian, North Indian</td>
      <td>300</td>
      <td>[('Rated 4.0', "RATED\n  Great food and proper...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_value</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>Grand Village</td>
      <td>No</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>166</td>
      <td>+91 8026612447\r\n+91 9901210005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Panipuri, Gol Gappe</td>
      <td>North Indian, Rajasthani</td>
      <td>600</td>
      <td>[('Rated 4.0', 'RATED\n  Very good restaurant ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Column_value</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51712</th>
      <td>https://www.zomato.com/bangalore/best-brews-fo...</td>
      <td>Four Points by Sheraton Bengaluru, 43/3, White...</td>
      <td>Best Brews - Four Points by Sheraton Bengaluru...</td>
      <td>No</td>
      <td>No</td>
      <td>3.6 /5</td>
      <td>27</td>
      <td>080 40301477</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', "RATED\n  Food and service are ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_value</td>
    </tr>
    <tr>
      <th>51713</th>
      <td>https://www.zomato.com/bangalore/vinod-bar-and...</td>
      <td>Number 10, Garudachar Palya, Mahadevapura, Whi...</td>
      <td>Vinod Bar And Restaurant</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>+91 8197675843</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>600</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_value</td>
    </tr>
    <tr>
      <th>51714</th>
      <td>https://www.zomato.com/bangalore/plunge-sherat...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Plunge - Sheraton Grand Bengaluru Whitefield H...</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>2,000</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_value</td>
    </tr>
    <tr>
      <th>51715</th>
      <td>https://www.zomato.com/bangalore/chime-sherato...</td>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>Chime - Sheraton Grand Bengaluru Whitefield Ho...</td>
      <td>No</td>
      <td>Yes</td>
      <td>4.3 /5</td>
      <td>236</td>
      <td>080 49652769</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar</td>
      <td>Cocktails, Pizza, Buttermilk</td>
      <td>Finger Food</td>
      <td>2,500</td>
      <td>[('Rated 4.0', 'RATED\n  Nice and friendly pla...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_value</td>
    </tr>
    <tr>
      <th>51716</th>
      <td>https://www.zomato.com/bangalore/the-nest-the-...</td>
      <td>ITPL Main Road, KIADB Export Promotion Industr...</td>
      <td>The Nest - The Den Bengaluru</td>
      <td>No</td>
      <td>No</td>
      <td>3.4 /5</td>
      <td>13</td>
      <td>+91 8071117272</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>NaN</td>
      <td>Finger Food, North Indian, Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', 'RATED\n  Great ambience , look...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Column_value</td>
    </tr>
  </tbody>
</table>
<p>51717 rows × 18 columns</p>
</div>




```python
zm.columns
```




    Index(['url', 'address', 'name', 'online_order', 'book_table', 'rate', 'votes',
           'phone', 'location', 'rest_type', 'dish_liked', 'cuisines',
           'approx_cost(for two people)', 'reviews_list', 'menu_item',
           'listed_in(type)', 'listed_in(city)', 'Values'],
          dtype='object')



## Reordering


```python
# 'url', 'address', 'name', 'online_order', 'book_table', 'rate', 'votes','phone', 'location', 'rest_type', 'dish_liked', 'cuisines','approx_cost(for two people)', 'reviews_list', 'menu_item','listed_in(type)', 'listed_in(city)', 'Values'
zm = zm[['address', 'url', 'Values', 'online_order', 'book_table', 'rate', 'votes',
       'phone', 'location', 'rest_type', 'dish_liked', 'cuisines',
       'approx_cost(for two people)', 'reviews_list', 'menu_item',
       'listed_in(type)', 'listed_in(city)', 'name']]
```


```python
# Here is reordering is done
zm  

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
      <th>url</th>
      <th>Values</th>
      <th>online_order</th>
      <th>book_table</th>
      <th>rate</th>
      <th>votes</th>
      <th>phone</th>
      <th>location</th>
      <th>rest_type</th>
      <th>dish_liked</th>
      <th>cuisines</th>
      <th>approx_cost(for two people)</th>
      <th>reviews_list</th>
      <th>menu_item</th>
      <th>listed_in(type)</th>
      <th>listed_in(city)</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>
      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>
      <td>Column_value</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>4.1/5</td>
      <td>775</td>
      <td>080 42297555\r\n+91 9743772233</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>
      <td>North Indian, Mughlai, Chinese</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  A beautiful place to ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Jalsa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>
      <td>https://www.zomato.com/bangalore/spice-elephan...</td>
      <td>Column_value</td>
      <td>Yes</td>
      <td>No</td>
      <td>4.1/5</td>
      <td>787</td>
      <td>080 41714161</td>
      <td>Banashankari</td>
      <td>Casual Dining</td>
      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>
      <td>Chinese, North Indian, Thai</td>
      <td>800</td>
      <td>[('Rated 4.0', 'RATED\n  Had been here for din...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Spice Elephant</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1112, Next to KIMS Medical College, 17th Cross...</td>
      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>
      <td>Column_value</td>
      <td>Yes</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>918</td>
      <td>+91 9663487993</td>
      <td>Banashankari</td>
      <td>Cafe, Casual Dining</td>
      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>
      <td>Cafe, Mexican, Italian</td>
      <td>800</td>
      <td>[('Rated 3.0', "RATED\n  Ambience is not that ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>San Churro Cafe</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>
      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>
      <td>Column_value</td>
      <td>No</td>
      <td>No</td>
      <td>3.7/5</td>
      <td>88</td>
      <td>+91 9620009302</td>
      <td>Banashankari</td>
      <td>Quick Bites</td>
      <td>Masala Dosa</td>
      <td>South Indian, North Indian</td>
      <td>300</td>
      <td>[('Rated 4.0', "RATED\n  Great food and proper...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Addhuri Udupi Bhojana</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>
      <td>https://www.zomato.com/bangalore/grand-village...</td>
      <td>Column_value</td>
      <td>No</td>
      <td>No</td>
      <td>3.8/5</td>
      <td>166</td>
      <td>+91 8026612447\r\n+91 9901210005</td>
      <td>Basavanagudi</td>
      <td>Casual Dining</td>
      <td>Panipuri, Gol Gappe</td>
      <td>North Indian, Rajasthani</td>
      <td>600</td>
      <td>[('Rated 4.0', 'RATED\n  Very good restaurant ...</td>
      <td>[]</td>
      <td>Buffet</td>
      <td>Banashankari</td>
      <td>Grand Village</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51712</th>
      <td>Four Points by Sheraton Bengaluru, 43/3, White...</td>
      <td>https://www.zomato.com/bangalore/best-brews-fo...</td>
      <td>Column_value</td>
      <td>No</td>
      <td>No</td>
      <td>3.6 /5</td>
      <td>27</td>
      <td>080 40301477</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', "RATED\n  Food and service are ...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Best Brews - Four Points by Sheraton Bengaluru...</td>
    </tr>
    <tr>
      <th>51713</th>
      <td>Number 10, Garudachar Palya, Mahadevapura, Whi...</td>
      <td>https://www.zomato.com/bangalore/vinod-bar-and...</td>
      <td>Column_value</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>+91 8197675843</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>600</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Vinod Bar And Restaurant</td>
    </tr>
    <tr>
      <th>51714</th>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>https://www.zomato.com/bangalore/plunge-sherat...</td>
      <td>Column_value</td>
      <td>No</td>
      <td>No</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>Whitefield</td>
      <td>Bar</td>
      <td>NaN</td>
      <td>Finger Food</td>
      <td>2,000</td>
      <td>[]</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Plunge - Sheraton Grand Bengaluru Whitefield H...</td>
    </tr>
    <tr>
      <th>51715</th>
      <td>Sheraton Grand Bengaluru Whitefield Hotel &amp; Co...</td>
      <td>https://www.zomato.com/bangalore/chime-sherato...</td>
      <td>Column_value</td>
      <td>No</td>
      <td>Yes</td>
      <td>4.3 /5</td>
      <td>236</td>
      <td>080 49652769</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar</td>
      <td>Cocktails, Pizza, Buttermilk</td>
      <td>Finger Food</td>
      <td>2,500</td>
      <td>[('Rated 4.0', 'RATED\n  Nice and friendly pla...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>Chime - Sheraton Grand Bengaluru Whitefield Ho...</td>
    </tr>
    <tr>
      <th>51716</th>
      <td>ITPL Main Road, KIADB Export Promotion Industr...</td>
      <td>https://www.zomato.com/bangalore/the-nest-the-...</td>
      <td>Column_value</td>
      <td>No</td>
      <td>No</td>
      <td>3.4 /5</td>
      <td>13</td>
      <td>+91 8071117272</td>
      <td>ITPL Main Road, Whitefield</td>
      <td>Bar, Casual Dining</td>
      <td>NaN</td>
      <td>Finger Food, North Indian, Continental</td>
      <td>1,500</td>
      <td>[('Rated 5.0', 'RATED\n  Great ambience , look...</td>
      <td>[]</td>
      <td>Pubs and bars</td>
      <td>Whitefield</td>
      <td>The Nest - The Den Bengaluru</td>
    </tr>
  </tbody>
</table>
<p>51717 rows × 18 columns</p>
</div>



<div style = "  display : flex; justify-content: center; ">
    <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
   Appending and Resetting Index
    </h1>
   
 </div>
  <p> </p>


```python
data = {
    'Names' : ['vishal', 'sneha' , 'souchit'],
     'Ages' : [22 , 21 , 21]
}
a1= pd.DataFrame(data) 
display(a1)
data2 = {
    'Names' : ['sabayasachi', 'Aditya' , 'sachine'],
     'Ages' : [21 , 20 , 21]
}
a2=pd.DataFrame(data2)
display(a2)

```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>vishal</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sneha</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>souchit</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>sabayasachi</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aditya</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>sachine</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



```python
# Now do Append between a1 and a2
a3 = a1.append(a2)
a3
# here Index is also  appending so we reset the Index
```

    C:\Users\91896\AppData\Local\Temp\ipykernel_1900\3095871087.py:2: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
      a3 = a1.append(a2)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>vishal</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sneha</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>souchit</td>
      <td>21</td>
    </tr>
    <tr>
      <th>0</th>
      <td>sabayasachi</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aditya</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>sachine</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
con = pd.concat([a1 , a2])
display(con) #index problem here so
display(pd.concat([a1 , a2], ignore_index = True ,axis = 1))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>vishal</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sneha</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>souchit</td>
      <td>21</td>
    </tr>
    <tr>
      <th>0</th>
      <td>sabayasachi</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aditya</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>sachine</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>vishal</td>
      <td>22</td>
      <td>sabayasachi</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sneha</td>
      <td>21</td>
      <td>Aditya</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>souchit</td>
      <td>21</td>
      <td>sachine</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



```python
a3 = a3.reset_index()
a3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>Names</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>vishal</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>sneha</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>souchit</td>
      <td>21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>sabayasachi</td>
      <td>21</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>Aditya</td>
      <td>20</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>sachine</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Now we can remove index coloum 0 1 2 0 1 2

a3 = a3.drop('index' , axis =1)
a3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>vishal</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sneha</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>souchit</td>
      <td>21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>sabayasachi</td>
      <td>21</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aditya</td>
      <td>20</td>
    </tr>
    <tr>
      <th>5</th>
      <td>sachine</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



<div style = "  display : flex; justify-content: center; ">
    <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
    ILOC and LOC
    </h1>
   
 </div>
  <p>The loc() function is label based data selecting method which means that we have to pass the name of the row or column which we want to select.
   <ul> Here End Index is Inclusive</ul> 
    <br><br>
The iloc() function is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column. 
    <ul>Here End Index is Exclusive</ul>
</p>


```python
import pandas as pd
 
# creating a sample dataframe
data = pd.DataFrame({'Brand': ['Maruti', 'Hyundai', 'Tata',
                               'Mahindra', 'Maruti', 'Hyundai',
                               'Renault', 'Tata', 'Maruti'],
                     'Year': [2012, 2014, 2011, 2015, 2012,
                              2016, 2014, 2018, 2019],
                     'Kms Driven': [50000, 30000, 60000,
                                    25000, 10000, 46000,
                                    31000, 15000, 12000],
                     'City': ['Gurgaon', 'Delhi', 'Mumbai',
                              'Delhi', 'Mumbai', 'Delhi',
                              'Mumbai', 'Chennai',  'Ghaziabad'],
                     'Mileage':  [28, 27, 25, 26, 28,
                                  29, 24, 21, 24]})
 
# displaying the DataFrame

display(data)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Brand</th>
      <th>Year</th>
      <th>Kms Driven</th>
      <th>City</th>
      <th>Mileage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Maruti</td>
      <td>2012</td>
      <td>50000</td>
      <td>Gurgaon</td>
      <td>28</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Hyundai</td>
      <td>2014</td>
      <td>30000</td>
      <td>Delhi</td>
      <td>27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tata</td>
      <td>2011</td>
      <td>60000</td>
      <td>Mumbai</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mahindra</td>
      <td>2015</td>
      <td>25000</td>
      <td>Delhi</td>
      <td>26</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Maruti</td>
      <td>2012</td>
      <td>10000</td>
      <td>Mumbai</td>
      <td>28</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hyundai</td>
      <td>2016</td>
      <td>46000</td>
      <td>Delhi</td>
      <td>29</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Renault</td>
      <td>2014</td>
      <td>31000</td>
      <td>Mumbai</td>
      <td>24</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Tata</td>
      <td>2018</td>
      <td>15000</td>
      <td>Chennai</td>
      <td>21</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Maruti</td>
      <td>2019</td>
      <td>12000</td>
      <td>Ghaziabad</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>



```python
display(data.iloc[1])
d1 = data.iloc[[1,2,8]]
display(d1)
display(data.iloc[1:5 ,  1:4]) # here 5 & 4 is excluded
# Means in iloc it work whole things in index wise
display(data.iloc[[1,4,8],[0,2,4]])
print('display(data.iloc[[1,4,8],[0,2,4]])')
```


    Brand         Hyundai
    Year             2014
    Kms Driven      30000
    City            Delhi
    Mileage            27
    Name: 1, dtype: object



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Brand</th>
      <th>Year</th>
      <th>Kms Driven</th>
      <th>City</th>
      <th>Mileage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Hyundai</td>
      <td>2014</td>
      <td>30000</td>
      <td>Delhi</td>
      <td>27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tata</td>
      <td>2011</td>
      <td>60000</td>
      <td>Mumbai</td>
      <td>25</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Maruti</td>
      <td>2019</td>
      <td>12000</td>
      <td>Ghaziabad</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Kms Driven</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2014</td>
      <td>30000</td>
      <td>Delhi</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2011</td>
      <td>60000</td>
      <td>Mumbai</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>25000</td>
      <td>Delhi</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2012</td>
      <td>10000</td>
      <td>Mumbai</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Brand</th>
      <th>Kms Driven</th>
      <th>Mileage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Hyundai</td>
      <td>30000</td>
      <td>27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Maruti</td>
      <td>10000</td>
      <td>28</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Maruti</td>
      <td>12000</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>


    display(data.iloc[[1,4,8],[0,2,4]])
    


```python
# loc
display(data.loc[data.Brand == 'Tata']) # ******
# display(data.loc[0:6, 2:3])       -> this will get an Error
display(data.loc[0:4]) # Here 4 is included
display(data.loc[0:4 , 'Year' : 'City'])
#  means in loc it work whole things in Name wise.
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Brand</th>
      <th>Year</th>
      <th>Kms Driven</th>
      <th>City</th>
      <th>Mileage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Tata</td>
      <td>2011</td>
      <td>60000</td>
      <td>Mumbai</td>
      <td>25</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Tata</td>
      <td>2018</td>
      <td>15000</td>
      <td>Chennai</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Brand</th>
      <th>Year</th>
      <th>Kms Driven</th>
      <th>City</th>
      <th>Mileage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Maruti</td>
      <td>2012</td>
      <td>50000</td>
      <td>Gurgaon</td>
      <td>28</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Hyundai</td>
      <td>2014</td>
      <td>30000</td>
      <td>Delhi</td>
      <td>27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tata</td>
      <td>2011</td>
      <td>60000</td>
      <td>Mumbai</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mahindra</td>
      <td>2015</td>
      <td>25000</td>
      <td>Delhi</td>
      <td>26</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Maruti</td>
      <td>2012</td>
      <td>10000</td>
      <td>Mumbai</td>
      <td>28</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Kms Driven</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012</td>
      <td>50000</td>
      <td>Gurgaon</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014</td>
      <td>30000</td>
      <td>Delhi</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2011</td>
      <td>60000</td>
      <td>Mumbai</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>25000</td>
      <td>Delhi</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2012</td>
      <td>10000</td>
      <td>Mumbai</td>
    </tr>
  </tbody>
</table>
</div>



```python
data.loc[(data.Brand == 'Hyundai') | (data.Brand == 'Tata')&(data.Mileage > 25)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Brand</th>
      <th>Year</th>
      <th>Kms Driven</th>
      <th>City</th>
      <th>Mileage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Hyundai</td>
      <td>2014</td>
      <td>30000</td>
      <td>Delhi</td>
      <td>27</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hyundai</td>
      <td>2016</td>
      <td>46000</td>
      <td>Delhi</td>
      <td>29</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.loc[(data.Brand == 'Hyundai') | (data.Brand == 'Tata')&(data.Mileage > 25)][['Mileage' , 'Year' , 'Kms Driven']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mileage</th>
      <th>Year</th>
      <th>Kms Driven</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>27</td>
      <td>2014</td>
      <td>30000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>29</td>
      <td>2016</td>
      <td>46000</td>
    </tr>
  </tbody>
</table>
</div>



<div style = "  display : flex; justify-content: center; ">
    <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
    Dropping Duplicates and Group by Function
    </h1>
   
 </div>
  <p> 
</p>

drop_duplicates it contain two parameter:

    1. subset -> Subset takes a column or list of column label. It’s default value is none. After passing columns, it will 
                 consider them only for duplicates. 
    2. keep = keep is to control how to consider duplicate value. It has only three distinct value and default is `first` 
              
              false, first ,last 


```python

data.drop_duplicates() # It is now consider duplicates according to index
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Brand</th>
      <th>Year</th>
      <th>Kms Driven</th>
      <th>City</th>
      <th>Mileage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Maruti</td>
      <td>2012</td>
      <td>50000</td>
      <td>Gurgaon</td>
      <td>28</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Hyundai</td>
      <td>2014</td>
      <td>30000</td>
      <td>Delhi</td>
      <td>27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tata</td>
      <td>2011</td>
      <td>60000</td>
      <td>Mumbai</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mahindra</td>
      <td>2015</td>
      <td>25000</td>
      <td>Delhi</td>
      <td>26</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Maruti</td>
      <td>2012</td>
      <td>10000</td>
      <td>Mumbai</td>
      <td>28</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hyundai</td>
      <td>2016</td>
      <td>46000</td>
      <td>Delhi</td>
      <td>29</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Renault</td>
      <td>2014</td>
      <td>31000</td>
      <td>Mumbai</td>
      <td>24</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Tata</td>
      <td>2018</td>
      <td>15000</td>
      <td>Chennai</td>
      <td>21</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Maruti</td>
      <td>2019</td>
      <td>12000</td>
      <td>Ghaziabad</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = {
    'Names' : ['vishal', 'sneha' , 'souchit'],
     'Ages' : [22 , 21 , 21]
}
a1= pd.DataFrame(data) 
display(a1)
data2 = {
    'Names' : ['vishal', 'Aditya' , 'sachine'],
     'Ages' : [22 , 20 , 21]
}
a2=pd.DataFrame(data2)
display(a2)
d1 = a1.append(a2)
display(d1)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>vishal</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sneha</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>souchit</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>vishal</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aditya</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>sachine</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>


    C:\Users\91896\AppData\Local\Temp\ipykernel_1900\1619079487.py:13: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
      d1 = a1.append(a2)
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>vishal</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sneha</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>souchit</td>
      <td>21</td>
    </tr>
    <tr>
      <th>0</th>
      <td>vishal</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aditya</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>sachine</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



```python
d1.drop_duplicates()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>vishal</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sneha</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>souchit</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aditya</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>sachine</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas as pd
  
data = {
    "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
    "B": [50, 40, 40, 30, 50],
    "C": [True, False, False, False, True]
}
  
df = pd.DataFrame(data)
display(df)
display(df.drop_duplicates())

```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TeamA</td>
      <td>50</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TeamB</td>
      <td>40</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TeamB</td>
      <td>40</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TeamC</td>
      <td>30</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TeamA</td>
      <td>50</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TeamA</td>
      <td>50</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TeamB</td>
      <td>40</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TeamC</td>
      <td>30</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



```python

```


```python
em = pd.read_csv('ExcelFile/Employees.csv')
display('Emlpoyees File',em)        

```


    'Emlpoyees File'



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Gender</th>
      <th>Start Date</th>
      <th>Last Login Time</th>
      <th>Salary</th>
      <th>Bonus %</th>
      <th>Senior Management</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Douglas</td>
      <td>Male</td>
      <td>8/6/1993</td>
      <td>12:42 PM</td>
      <td>97308</td>
      <td>6.945</td>
      <td>True</td>
      <td>Marketing</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Thomas</td>
      <td>Male</td>
      <td>3/31/1996</td>
      <td>6:53 AM</td>
      <td>61933</td>
      <td>4.170</td>
      <td>True</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Maria</td>
      <td>Female</td>
      <td>4/23/1993</td>
      <td>11:17 AM</td>
      <td>130590</td>
      <td>11.858</td>
      <td>False</td>
      <td>Finance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jerry</td>
      <td>Male</td>
      <td>3/4/2005</td>
      <td>1:00 PM</td>
      <td>138705</td>
      <td>9.340</td>
      <td>True</td>
      <td>Finance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Larry</td>
      <td>Male</td>
      <td>1/24/1998</td>
      <td>4:47 PM</td>
      <td>101004</td>
      <td>1.389</td>
      <td>True</td>
      <td>Client Services</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>995</th>
      <td>Henry</td>
      <td>NaN</td>
      <td>11/23/2014</td>
      <td>6:09 AM</td>
      <td>132483</td>
      <td>16.655</td>
      <td>False</td>
      <td>Distribution</td>
    </tr>
    <tr>
      <th>996</th>
      <td>Phillip</td>
      <td>Male</td>
      <td>1/31/1984</td>
      <td>6:30 AM</td>
      <td>42392</td>
      <td>19.675</td>
      <td>False</td>
      <td>Finance</td>
    </tr>
    <tr>
      <th>997</th>
      <td>Russell</td>
      <td>Male</td>
      <td>5/20/2013</td>
      <td>12:39 PM</td>
      <td>96914</td>
      <td>1.421</td>
      <td>False</td>
      <td>Product</td>
    </tr>
    <tr>
      <th>998</th>
      <td>Larry</td>
      <td>Male</td>
      <td>4/20/2013</td>
      <td>4:45 PM</td>
      <td>60500</td>
      <td>11.985</td>
      <td>False</td>
      <td>Business Development</td>
    </tr>
    <tr>
      <th>999</th>
      <td>Albert</td>
      <td>Male</td>
      <td>5/15/2012</td>
      <td>6:24 PM</td>
      <td>129949</td>
      <td>10.169</td>
      <td>True</td>
      <td>Sales</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 8 columns</p>
</div>



```python
# sorting by first name
em = em.sort_values("First Name")
display('Sorting By First Name',em)
```


    'Sorting By First Name'



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Gender</th>
      <th>Start Date</th>
      <th>Last Login Time</th>
      <th>Salary</th>
      <th>Bonus %</th>
      <th>Senior Management</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>101</th>
      <td>Aaron</td>
      <td>Male</td>
      <td>2/17/2012</td>
      <td>10:20 AM</td>
      <td>61602</td>
      <td>11.849</td>
      <td>True</td>
      <td>Marketing</td>
    </tr>
    <tr>
      <th>327</th>
      <td>Aaron</td>
      <td>Male</td>
      <td>1/29/1994</td>
      <td>6:48 PM</td>
      <td>58755</td>
      <td>5.097</td>
      <td>True</td>
      <td>Marketing</td>
    </tr>
    <tr>
      <th>440</th>
      <td>Aaron</td>
      <td>Male</td>
      <td>7/22/1990</td>
      <td>2:53 PM</td>
      <td>52119</td>
      <td>11.343</td>
      <td>True</td>
      <td>Client Services</td>
    </tr>
    <tr>
      <th>937</th>
      <td>Aaron</td>
      <td>NaN</td>
      <td>1/22/1986</td>
      <td>7:39 PM</td>
      <td>63126</td>
      <td>18.424</td>
      <td>False</td>
      <td>Client Services</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Adam</td>
      <td>Male</td>
      <td>5/21/2011</td>
      <td>1:45 AM</td>
      <td>95327</td>
      <td>15.120</td>
      <td>False</td>
      <td>Distribution</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>902</th>
      <td>NaN</td>
      <td>Male</td>
      <td>5/23/2001</td>
      <td>7:52 PM</td>
      <td>103877</td>
      <td>6.322</td>
      <td>NaN</td>
      <td>Distribution</td>
    </tr>
    <tr>
      <th>925</th>
      <td>NaN</td>
      <td>Female</td>
      <td>8/23/2000</td>
      <td>4:19 PM</td>
      <td>95866</td>
      <td>19.388</td>
      <td>NaN</td>
      <td>Sales</td>
    </tr>
    <tr>
      <th>946</th>
      <td>NaN</td>
      <td>Female</td>
      <td>9/15/1985</td>
      <td>1:50 AM</td>
      <td>133472</td>
      <td>16.941</td>
      <td>NaN</td>
      <td>Distribution</td>
    </tr>
    <tr>
      <th>947</th>
      <td>NaN</td>
      <td>Male</td>
      <td>7/30/2012</td>
      <td>3:07 PM</td>
      <td>107351</td>
      <td>5.329</td>
      <td>NaN</td>
      <td>Marketing</td>
    </tr>
    <tr>
      <th>951</th>
      <td>NaN</td>
      <td>Female</td>
      <td>9/14/2010</td>
      <td>5:19 AM</td>
      <td>143638</td>
      <td>9.662</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 8 columns</p>
</div>



```python
# To remove All Duplicates from file.
em.drop_duplicates(subset = "First Name" , inplace = True)
display('Duplicates only in First Name Column',em)  # here all dublicates in first Name have removed
```


    'Duplicates only in First Name Column'



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Gender</th>
      <th>Start Date</th>
      <th>Last Login Time</th>
      <th>Salary</th>
      <th>Bonus %</th>
      <th>Senior Management</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>101</th>
      <td>Aaron</td>
      <td>Male</td>
      <td>2/17/2012</td>
      <td>10:20 AM</td>
      <td>61602</td>
      <td>11.849</td>
      <td>True</td>
      <td>Marketing</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Adam</td>
      <td>Male</td>
      <td>5/21/2011</td>
      <td>1:45 AM</td>
      <td>95327</td>
      <td>15.120</td>
      <td>False</td>
      <td>Distribution</td>
    </tr>
    <tr>
      <th>300</th>
      <td>Alan</td>
      <td>Male</td>
      <td>6/26/1988</td>
      <td>3:54 AM</td>
      <td>111786</td>
      <td>3.592</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>372</th>
      <td>Albert</td>
      <td>Male</td>
      <td>2/1/1997</td>
      <td>4:20 PM</td>
      <td>67827</td>
      <td>19.717</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>988</th>
      <td>Alice</td>
      <td>Female</td>
      <td>10/5/2004</td>
      <td>9:34 AM</td>
      <td>47638</td>
      <td>11.209</td>
      <td>False</td>
      <td>Human Resources</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>433</th>
      <td>Wanda</td>
      <td>Female</td>
      <td>7/20/2008</td>
      <td>1:44 PM</td>
      <td>65362</td>
      <td>7.132</td>
      <td>True</td>
      <td>Legal</td>
    </tr>
    <tr>
      <th>177</th>
      <td>Wayne</td>
      <td>Male</td>
      <td>4/7/2012</td>
      <td>8:00 AM</td>
      <td>102652</td>
      <td>14.085</td>
      <td>True</td>
      <td>Distribution</td>
    </tr>
    <tr>
      <th>820</th>
      <td>William</td>
      <td>Male</td>
      <td>11/18/1993</td>
      <td>12:27 PM</td>
      <td>54058</td>
      <td>5.182</td>
      <td>True</td>
      <td>Human Resources</td>
    </tr>
    <tr>
      <th>450</th>
      <td>Willie</td>
      <td>Male</td>
      <td>8/22/2009</td>
      <td>1:03 PM</td>
      <td>55038</td>
      <td>19.691</td>
      <td>False</td>
      <td>Legal</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>Female</td>
      <td>7/20/2015</td>
      <td>10:43 AM</td>
      <td>45906</td>
      <td>11.598</td>
      <td>NaN</td>
      <td>Finance</td>
    </tr>
  </tbody>
</table>
<p>201 rows × 8 columns</p>
</div>



```python
display('Remove ALL duplicates')
em.drop_duplicates(subset = "First Name" , keep = False ,inplace=True  )
display(em)
```


    'Remove ALL duplicates'



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Gender</th>
      <th>Start Date</th>
      <th>Last Login Time</th>
      <th>Salary</th>
      <th>Bonus %</th>
      <th>Senior Management</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>101</th>
      <td>Aaron</td>
      <td>Male</td>
      <td>2/17/2012</td>
      <td>10:20 AM</td>
      <td>61602</td>
      <td>11.849</td>
      <td>True</td>
      <td>Marketing</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Adam</td>
      <td>Male</td>
      <td>5/21/2011</td>
      <td>1:45 AM</td>
      <td>95327</td>
      <td>15.120</td>
      <td>False</td>
      <td>Distribution</td>
    </tr>
    <tr>
      <th>300</th>
      <td>Alan</td>
      <td>Male</td>
      <td>6/26/1988</td>
      <td>3:54 AM</td>
      <td>111786</td>
      <td>3.592</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>372</th>
      <td>Albert</td>
      <td>Male</td>
      <td>2/1/1997</td>
      <td>4:20 PM</td>
      <td>67827</td>
      <td>19.717</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>988</th>
      <td>Alice</td>
      <td>Female</td>
      <td>10/5/2004</td>
      <td>9:34 AM</td>
      <td>47638</td>
      <td>11.209</td>
      <td>False</td>
      <td>Human Resources</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>433</th>
      <td>Wanda</td>
      <td>Female</td>
      <td>7/20/2008</td>
      <td>1:44 PM</td>
      <td>65362</td>
      <td>7.132</td>
      <td>True</td>
      <td>Legal</td>
    </tr>
    <tr>
      <th>177</th>
      <td>Wayne</td>
      <td>Male</td>
      <td>4/7/2012</td>
      <td>8:00 AM</td>
      <td>102652</td>
      <td>14.085</td>
      <td>True</td>
      <td>Distribution</td>
    </tr>
    <tr>
      <th>820</th>
      <td>William</td>
      <td>Male</td>
      <td>11/18/1993</td>
      <td>12:27 PM</td>
      <td>54058</td>
      <td>5.182</td>
      <td>True</td>
      <td>Human Resources</td>
    </tr>
    <tr>
      <th>450</th>
      <td>Willie</td>
      <td>Male</td>
      <td>8/22/2009</td>
      <td>1:03 PM</td>
      <td>55038</td>
      <td>19.691</td>
      <td>False</td>
      <td>Legal</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>Female</td>
      <td>7/20/2015</td>
      <td>10:43 AM</td>
      <td>45906</td>
      <td>11.598</td>
      <td>NaN</td>
      <td>Finance</td>
    </tr>
  </tbody>
</table>
<p>201 rows × 8 columns</p>
</div>



```python
group = em.groupby('Team')
display(pd.DataFrame(group))
for i in  group:
    display(i)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Business Development</td>
      <td>First Name  Gender  Start Date Last Login ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Client Services</td>
      <td>First Name  Gender  Start Date Last Login ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Distribution</td>
      <td>First Name  Gender  Start Date Last Login ...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Engineering</td>
      <td>First Name  Gender  Start Date Last Login ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Finance</td>
      <td>First Name  Gender  Start Date Last Login ...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Human Resources</td>
      <td>First Name  Gender  Start Date Last Login ...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Legal</td>
      <td>First Name  Gender  Start Date Last Login...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Marketing</td>
      <td>First Name  Gender  Start Date Last Login ...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Product</td>
      <td>First Name  Gender  Start Date Last Login ...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Sales</td>
      <td>First Name  Gender  Start Date Last Logi...</td>
    </tr>
  </tbody>
</table>
</div>



    ('Business Development',
         First Name  Gender  Start Date Last Login Time  Salary  Bonus %  \
     509        Ann  Female   11/4/1984        12:17 PM   90719    6.220   
     129    Antonio    Male  10/25/1988         1:50 PM   60866   13.101   
     735    Barbara  Female  11/26/2002         5:32 AM   82884    6.837   
     872     Brenda  Female   1/18/2015         4:39 PM   73749   19.332   
     487     Cheryl  Female   12/3/2014         9:27 AM   71751   15.918   
     48    Clarence    Male   3/26/1996         5:57 AM   93581    6.083   
     203      Diana  Female    1/4/2013         7:53 AM  103521    2.784   
     583      Diane  Female    2/2/1988         6:14 PM   49501   13.506   
     779      Doris  Female    9/8/1984         7:03 PM  114360   17.799   
     419    Dorothy  Female   11/5/2013        10:50 PM  140136    3.120   
     746     Gloria  Female   8/19/2004        10:31 AM   46602    1.027   
     99      Harold    Male    1/2/1985         9:40 PM   77544   12.447   
     745      James    Male   2/16/2008         2:49 AM   69111   14.625   
     33        Jean  Female  12/18/1993         9:07 AM  119082   16.180   
     928    Jeffrey    Male   9/20/1986         6:06 AM  111376    2.673   
     64    Kathleen     NaN   4/11/1990         6:46 PM   77834   18.771   
     411      Kevin    Male   6/23/1981         8:26 PM  134598   11.699   
     772    Lillian  Female   8/14/2009         5:41 AM  113554   18.018   
     936      Maria  Female   3/14/2003         5:23 PM   96250   10.056   
     916    Marilyn  Female   1/16/1996         7:18 AM  118369    7.696   
     306       Mark    Male    4/1/1984         1:21 PM  121477   17.440   
     748     Martha  Female   7/17/1997        11:11 PM   94963   19.626   
     788   Michelle     NaN   3/31/2012         6:28 AM  124441   16.353   
     401      Norma  Female   4/16/1996         5:40 AM   38872    9.302   
     971    Patrick    Male  12/30/2002         2:01 AM   75423    5.368   
     673      Ralph    Male   3/24/1996        11:54 AM   50455   16.248   
     841       Ruby  Female   8/13/2006         6:27 PM   48354   19.501   
     
         Senior Management                  Team  
     509             False  Business Development  
     129              True  Business Development  
     735              True  Business Development  
     872             False  Business Development  
     487             False  Business Development  
     48               True  Business Development  
     203              True  Business Development  
     583             False  Business Development  
     779              True  Business Development  
     419              True  Business Development  
     746              True  Business Development  
     99              False  Business Development  
     745              True  Business Development  
     33              False  Business Development  
     928              True  Business Development  
     64              False  Business Development  
     411             False  Business Development  
     772              True  Business Development  
     936             False  Business Development  
     916              True  Business Development  
     306              True  Business Development  
     748              True  Business Development  
     788             False  Business Development  
     401              True  Business Development  
     971              True  Business Development  
     673             False  Business Development  
     841             False  Business Development  )



    ('Client Services',
         First Name  Gender  Start Date Last Login Time  Salary  Bonus %  \
     639     Amanda     NaN   8/11/1991         2:15 PM   46665   19.391   
     879        Amy  Female   5/20/2009         6:26 AM   75415   19.132   
     564     Andrew    Male   3/29/1985         6:57 PM   43414    7.563   
     282       Carl     NaN    2/7/2014         3:57 AM  125104   12.345   
     197    Carolyn  Female   11/6/2012         3:51 AM   69268    3.031   
     95     Heather  Female   7/11/1998         2:17 PM   43026   14.166   
     22      Joshua     NaN    3/8/2012         1:58 AM   90816   18.816   
     4        Larry    Male   1/24/1998         4:47 PM  101004    1.389   
     679       Lori  Female   9/11/2002         7:36 AM   66029    3.345   
     742     Martin    Male   2/25/2016         6:29 PM   61117    2.844   
     606    Mildred  Female   2/21/1981         3:30 AM   47266   10.256   
     605       Rose  Female   5/20/1982         9:14 AM   97691    2.142   
     918       Ryan    Male   4/27/1999         3:41 AM   85858   19.475   
     489     Sharon  Female    7/1/2011         9:50 AM   46007   19.731   
     291      Tammy  Female  11/11/1984        10:30 AM  132839   17.463   
     
         Senior Management             Team  
     639              True  Client Services  
     879             False  Client Services  
     564              True  Client Services  
     282             False  Client Services  
     197             False  Client Services  
     95              False  Client Services  
     22               True  Client Services  
     4                True  Client Services  
     679              True  Client Services  
     742             False  Client Services  
     606             False  Client Services  
     605             False  Client Services  
     918             False  Client Services  
     489              True  Client Services  
     291              True  Client Services  )



    ('Distribution',
         First Name  Gender  Start Date Last Login Time  Salary  Bonus %  \
     137       Adam    Male   5/21/2011         1:45 AM   95327   15.120   
     430     Andrea  Female   10/1/2010        11:54 AM   79123   19.422   
     838      Billy    Male    4/6/2000         3:14 PM  115280    9.153   
     522  Catherine  Female   8/31/2013         7:24 PM   58047   14.858   
     614       Eric    Male  11/12/2004         9:16 PM   65168   11.513   
     486     Howard    Male    4/9/2012         6:36 AM   37984    2.021   
     566     Johnny    Male    1/8/1995         1:35 PM   91124   12.986   
     248     Justin    Male   12/6/1992         5:58 PM   82782    4.366   
     616   Kimberly  Female   12/6/1986         2:23 PM   37916   12.929   
     76    Margaret  Female   9/10/1988        12:42 PM  131604    7.353   
     830    Michael    Male   8/31/2002         1:20 AM   81206   19.908   
     60       Paula     NaN  11/23/2005         2:01 PM   48866    4.271   
     591     Rachel  Female   4/22/1988        12:01 PM  110924    7.808   
     181      Randy    Male  11/14/1999        12:12 PM   58129    1.952   
     759       Ruth  Female    9/2/1980         6:52 AM   59678   10.895   
     882       Sara     NaN  11/18/2014         2:47 PM  135990   14.344   
     501       Sean    Male   2/11/2013         7:07 PM   42748    9.765   
     804      Shawn    Male   3/17/2008         2:12 PM   39335   10.664   
     756    Stephen    Male  10/21/1984         6:26 AM  121816   10.615   
     762      Terry    Male  11/10/2004         4:33 AM   35633    3.947   
     294   Virginia  Female  10/20/1999         6:23 AM   46905   19.154   
     288     Walter     NaN  12/21/1999        10:33 PM   66757   18.099   
     177      Wayne    Male    4/7/2012         8:00 AM  102652   14.085   
     
         Senior Management          Team  
     137             False  Distribution  
     430             False  Distribution  
     838             False  Distribution  
     522              True  Distribution  
     614             False  Distribution  
     486             False  Distribution  
     566              True  Distribution  
     248              True  Distribution  
     616              True  Distribution  
     76               True  Distribution  
     830              True  Distribution  
     60              False  Distribution  
     591             False  Distribution  
     181              True  Distribution  
     759             False  Distribution  
     882              True  Distribution  
     501             False  Distribution  
     804             False  Distribution  
     756              True  Distribution  
     762              True  Distribution  
     294             False  Distribution  
     288             False  Distribution  
     177              True  Distribution  )



    ('Engineering',
         First Name  Gender  Start Date Last Login Time  Salary  Bonus %  \
     300       Alan    Male   6/26/1988         3:54 AM  111786    3.592   
     372     Albert    Male    2/1/1997         4:20 PM   67827   19.717   
     8       Angela  Female  11/22/2005         6:29 AM   95570   18.523   
     262       Anne  Female   7/16/1986         2:08 PM   69134    3.723   
     138     Ashley  Female   5/25/2006        11:30 AM  112238    6.030   
     956    Beverly  Female  10/17/1986        12:51 AM   80838    8.115   
     604      Bruce    Male   3/15/2013        11:13 PM  141335   15.427   
     456    Deborah     NaN    2/3/1983        11:38 PM  101457    6.662   
     615     Edward    Male   8/30/2001         1:24 AM   73105    6.083   
     209      Emily  Female   9/20/2007        11:25 AM   89434   11.295   
     908     Janice  Female  12/17/2009         6:42 AM  102697    3.283   
     761   Jennifer  Female   3/31/2015         7:43 PM  132084   10.006   
     719       John    Male   1/29/1999         3:07 AM   67165   13.001   
     474   Jonathan    Male   8/15/2002        12:01 AM  104749   11.364   
     214      Julie  Female   7/23/1989         1:52 PM  109588    3.550   
     816      Kelly  Female   3/17/2007         6:20 PM   39371    4.068   
     558      Linda  Female   8/18/1985         4:34 AM   51431   13.295   
     191       Lois  Female  10/18/2013         4:51 PM   36946    6.652   
     50       Nancy  Female   9/23/2000         8:05 AM   94976   13.830   
     707   Patricia  Female    3/7/1998         1:10 AM   75825    7.839   
     551     Philip    Male   7/18/1985         6:36 AM  122319   19.122   
     632    Rebecca  Female   2/23/1990         3:21 PM  134673    6.878   
     402    Richard     NaN  11/28/1992         5:05 PM  124655   14.272   
     475  Stephanie  Female  11/26/1992        12:54 AM  122121    7.937   
     967     Thomas    Male   3/12/2016         3:10 PM  105681   19.572   
     113       Tina  Female   6/12/2009         7:16 AM  114767    3.711   
     
         Senior Management         Team  
     300              True  Engineering  
     372              True  Engineering  
     8                True  Engineering  
     262              True  Engineering  
     138              True  Engineering  
     956             False  Engineering  
     604              True  Engineering  
     456             False  Engineering  
     615              True  Engineering  
     209             False  Engineering  
     908             False  Engineering  
     761              True  Engineering  
     719             False  Engineering  
     474             False  Engineering  
     214             False  Engineering  
     816             False  Engineering  
     558             False  Engineering  
     191             False  Engineering  
     50               True  Engineering  
     707             False  Engineering  
     551             False  Engineering  
     632             False  Engineering  
     402              True  Engineering  
     475              True  Engineering  
     967             False  Engineering  
     113              True  Engineering  )



    ('Finance',
         First Name  Gender  Start Date Last Login Time  Salary  Bonus %  \
     341     Carlos    Male   9/19/2007         1:01 AM   77327   11.580   
     190      Carol  Female   3/19/1996         3:39 AM   57783    9.129   
     646  Elizabeth  Female   2/21/2010         7:02 AM   79145   19.780   
     311     Ernest     NaN   1/18/2002         1:51 AM   72145   13.448   
     200       Gary    Male   8/12/1987        12:04 AM   89661    8.525   
     809     George    Male   9/27/1995         5:04 PM   36749   19.754   
     861      Jerry    Male   3/26/1989         4:15 AM  140850   18.855   
     179    Jessica  Female  10/23/1995         5:53 AM   68759   19.343   
     691       Joan  Female   10/2/2007         2:53 AM  120941    3.694   
     418      Julia  Female    3/2/1982        12:52 PM   36403    2.664   
     618      Peter    Male  11/24/1992         5:43 PM   69297    1.268   
     103    Phyllis  Female  10/11/1996         9:30 PM  136984    8.932   
     613     Teresa     NaN    1/3/1992         3:47 PM   63103   11.378   
     7          NaN  Female   7/20/2015        10:43 AM   45906   11.598   
     
         Senior Management     Team  
     341              True  Finance  
     190             False  Finance  
     646             False  Finance  
     311              True  Finance  
     200             False  Finance  
     809             False  Finance  
     861             False  Finance  
     179              True  Finance  
     691              True  Finance  
     418              True  Finance  
     618             False  Finance  
     103              True  Finance  
     613             False  Finance  
     7                 NaN  Finance  )



    ('Human Resources',
         First Name  Gender  Start Date Last Login Time  Salary  Bonus %  \
     988      Alice  Female   10/5/2004         9:34 AM   47638   11.209   
     776      Bobby    Male   9/30/2004        10:52 PM   79047   18.784   
     900  Christina  Female   6/23/2002         3:18 PM   35477   18.178   
     717      Jason     NaN   4/15/1988         8:16 PM   97480   11.518   
     839      Joyce  Female   7/25/2001         6:04 AM   51065   16.807   
     424    Matthew     NaN    6/9/2003         7:35 AM   79443   14.637   
     874    Melissa  Female    9/8/1994         4:11 AM   98858    3.525   
     439   Nicholas    Male    3/1/2013         9:26 PM  101036    2.826   
     589     Sandra  Female   4/24/1995         7:14 PM  116931    9.657   
     417      Sarah     NaN   8/31/1981         2:51 PM   37748    9.047   
     130    Shirley  Female    5/1/1984         1:15 PM   41334    6.219   
     525      Steve    Male   8/22/1995         6:58 AM   67780    9.540   
     743     Steven    Male   5/30/1980         8:25 PM  100949   13.813   
     795    Theresa     NaN   10/7/1995        10:16 AM   42025    3.319   
     820    William    Male  11/18/1993        12:27 PM   54058    5.182   
     
         Senior Management             Team  
     988             False  Human Resources  
     776             False  Human Resources  
     900             False  Human Resources  
     717             False  Human Resources  
     839             False  Human Resources  
     424             False  Human Resources  
     874              True  Human Resources  
     439              True  Human Resources  
     589              True  Human Resources  
     417             False  Human Resources  
     130              True  Human Resources  
     525              True  Human Resources  
     743              True  Human Resources  
     795              True  Human Resources  
     820              True  Human Resources  )



    ('Legal',
          First Name  Gender  Start Date Last Login Time  Salary  Bonus %  \
     688       Brian    Male    4/7/2007        10:47 PM   93901   17.821   
     431     Charles    Male  12/16/1999         8:28 PM  104014    7.077   
     500   Christine  Female    2/1/2003         1:11 PM   72613   11.126   
     223      Daniel    Male   4/30/2010         3:48 AM  106947   15.866   
     887       David    Male   12/5/2009         8:48 AM   92242   15.407   
     256       Debra  Female   3/13/1998        11:16 PM   48696    4.750   
     5        Dennis    Male   4/18/1987         1:35 AM  115163   10.125   
     94        Harry    Male   8/26/1981         3:16 PM  130620    7.030   
     136       Henry    Male   4/24/1995         4:18 AM   43542   19.687   
     412  Jacqueline  Female   2/11/2007         2:01 AM   66604   14.609   
     749       Janet     NaN   1/25/1986         5:48 AM   85789    9.712   
     827       Jesse     NaN   7/16/2014         2:24 AM   98811    7.487   
     791      Joseph    Male   11/4/1982         9:46 PM  126010   19.601   
     313        Judy  Female    7/1/1991         2:33 AM  109510   13.457   
     832       Keith    Male   2/12/2003         3:02 PM  120672   19.467   
     106        Paul    Male    8/4/1993         7:25 PM   42146    3.046   
     488      Robert    Male   3/11/2007        11:20 AM  135882   19.944   
     108     Russell     NaN    5/5/1988         7:57 AM  133980   12.396   
     664     Timothy    Male   10/6/2010        10:49 PM   49473   12.463   
     433       Wanda  Female   7/20/2008         1:44 PM   65362    7.132   
     450      Willie    Male   8/22/2009         1:03 PM   55038   19.691   
     
         Senior Management   Team  
     688              True  Legal  
     431             False  Legal  
     500             False  Legal  
     223              True  Legal  
     887             False  Legal  
     256             False  Legal  
     5               False  Legal  
     94              False  Legal  
     136             False  Legal  
     412             False  Legal  
     749             False  Legal  
     827             False  Legal  
     791             False  Legal  
     313              True  Legal  
     832             False  Legal  
     106             False  Legal  
     488             False  Legal  
     108              True  Legal  
     664             False  Legal  
     433              True  Legal  
     450             False  Legal  )



    ('Marketing',
         First Name  Gender  Start Date Last Login Time  Salary  Bonus %  \
     101      Aaron    Male   2/17/2012        10:20 AM   61602   11.849   
     645       Anna     NaN   3/13/1985         9:19 AM   45418   10.162   
     556     Arthur    Male  12/16/2014         4:56 PM   66819    6.639   
     894      Betty  Female  11/19/2002        10:40 AM   37005    7.645   
     26       Craig    Male   2/27/2000         7:45 AM   37598    7.757   
     331     Evelyn  Female    9/3/1983         1:58 PM   36759   17.269   
     490     Judith  Female  11/23/2007         1:22 PM  117055    7.461   
     656       Lisa  Female    2/9/1982         6:44 PM  113592   17.108   
     535     Louise  Female   9/18/1981         5:47 AM   91462    8.205   
     730     Nicole  Female   4/26/2009        12:40 AM   66047   18.674   
     187      Roger    Male  11/19/2004         3:55 PM   51430    6.460   
     696     Samuel    Male   5/25/2012         4:40 PM   85550   11.593   
     452      Scott    Male  11/17/2012         2:47 PM  146812    1.965   
     
         Senior Management       Team  
     101              True  Marketing  
     645             False  Marketing  
     556              True  Marketing  
     894              True  Marketing  
     26               True  Marketing  
     331              True  Marketing  
     490             False  Marketing  
     656              True  Marketing  
     535             False  Marketing  
     730              True  Marketing  
     187             False  Marketing  
     696              True  Marketing  
     452              True  Marketing  )



    ('Product',
         First Name  Gender  Start Date Last Login Time  Salary  Bonus %  \
     757   Benjamin    Male   4/12/1988        11:32 PM  123409    7.783   
     79      Bonnie  Female  11/13/1988         3:30 PM  115814    4.990   
     44     Cynthia  Female  11/16/1988         6:54 PM  145146    7.482   
     909     Donald    Male    8/1/1991         2:25 AM   61999    6.466   
     19       Donna  Female   7/22/2010         3:48 AM   81014    1.894   
     322    Douglas    Male    1/8/2002         6:42 PM   41428   14.372   
     533       Earl    Male   2/11/2014         9:03 PM   52620   13.773   
     681      Frank    Male  11/23/2002         6:10 PM   75147   17.398   
     272       Fred    Male   2/20/1980         2:25 AM   74129   18.225   
     123      Helen  Female  11/29/2001         2:30 AM   73789   14.841   
     384       Jack    Male  12/24/1980        10:58 PM  106995   15.723   
     178       Jane  Female    9/3/1997         2:01 AM  144474   17.648   
     463       Jose    Male   7/11/2002         9:15 AM   59862    3.269   
     364       Juan    Male   4/16/2002        11:09 PM   97364    3.595   
     55       Karen  Female  11/30/1999         7:46 AM  102488   17.653   
     868  Katherine  Female   8/18/2013         3:58 PM   97443   13.657   
     236      Laura  Female    4/2/2006         1:57 PM   42087    2.624   
     737   Lawrence    Male   7/23/2011         3:41 AM  122971   14.618   
     750      Louis     NaN    2/5/1983         6:39 PM  145274   16.379   
     261      Marie  Female    8/6/1995         1:58 PM  100308   13.677   
     369       Mary  Female  10/18/2009         6:32 PM   87721   12.484   
     115     Pamela  Female    7/1/1982         6:51 AM   54585    4.166   
     799    Raymond    Male  12/12/1986        12:18 PM   47529    2.712   
     394      Robin  Female    1/8/1998         2:12 AM  111163    5.025   
     422     Victor    Male   9/24/2005        12:04 PM  123144   16.261   
     
         Senior Management     Team  
     757             False  Product  
     79              False  Product  
     44               True  Product  
     909             False  Product  
     19              False  Product  
     322             False  Product  
     533             False  Product  
     681             False  Product  
     272             False  Product  
     123              True  Product  
     384             False  Product  
     178             False  Product  
     463             False  Product  
     364             False  Product  
     55               True  Product  
     868             False  Product  
     236             False  Product  
     737             False  Product  
     750             False  Product  
     261             False  Product  
     369             False  Product  
     115             False  Product  
     799              True  Product  
     394              True  Product  
     422              True  Product  )



    ('Sales',
           First Name  Gender  Start Date Last Login Time  Salary  Bonus %  \
     87         Annie  Female   1/30/1993         2:05 AM  144887    8.276   
     886      Anthony    Male   1/30/2014         9:04 PM   96795   14.837   
     892      Brandon    Male  10/23/1995        12:04 PM   60263    2.709   
     167  Christopher    Male  12/24/2011        12:22 PM  142178   17.984   
     437       Denise  Female   3/18/2001        12:02 AM   36697   11.196   
     495       Eugene    Male   5/24/1984        10:54 AM   81077    2.117   
     73       Frances  Female    4/4/1999         4:19 PM   90582    4.709   
     312       Gerald    Male   4/16/2001        10:09 PM  121604    1.923   
     375      Gregory     NaN    7/9/2011        11:31 PM  137661    4.805   
     622        Irene  Female   6/23/2005        11:03 AM   89780    8.999   
     624       Jeremy    Male  11/26/1997         8:22 AM  133033   12.200   
     806      Kathryn  Female   1/29/2008        12:29 AM   86676    6.081   
     443        Kathy  Female    5/8/1987         6:19 PM   86318   18.492   
     373      Kenneth    Male   4/13/1999        10:28 PM   81839   12.072   
     862       Ronald    Male   5/25/1983        10:05 AM   50426   18.536   
     727          Roy    Male   5/10/2004         1:22 PM   46875   12.942   
     975        Susan  Female    4/7/1995        10:05 PM   92436   12.467   
     609         Todd    Male   2/16/2010        11:29 AM  103405   15.910   
     
         Senior Management   Team  
     87               True  Sales  
     886             False  Sales  
     892             False  Sales  
     167              True  Sales  
     437              True  Sales  
     495             False  Sales  
     73               True  Sales  
     312              True  Sales  
     375              True  Sales  
     622              True  Sales  
     624             False  Sales  
     806             False  Sales  
     443              True  Sales  
     373             False  Sales  
     862              True  Sales  
     727              True  Sales  
     975             False  Sales  
     609             False  Sales  )



```python
display(group.get_group('Engineering'))
group.get_group('Engineering')['Salary']
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Gender</th>
      <th>Start Date</th>
      <th>Last Login Time</th>
      <th>Salary</th>
      <th>Bonus %</th>
      <th>Senior Management</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>300</th>
      <td>Alan</td>
      <td>Male</td>
      <td>6/26/1988</td>
      <td>3:54 AM</td>
      <td>111786</td>
      <td>3.592</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>372</th>
      <td>Albert</td>
      <td>Male</td>
      <td>2/1/1997</td>
      <td>4:20 PM</td>
      <td>67827</td>
      <td>19.717</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Angela</td>
      <td>Female</td>
      <td>11/22/2005</td>
      <td>6:29 AM</td>
      <td>95570</td>
      <td>18.523</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>262</th>
      <td>Anne</td>
      <td>Female</td>
      <td>7/16/1986</td>
      <td>2:08 PM</td>
      <td>69134</td>
      <td>3.723</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>138</th>
      <td>Ashley</td>
      <td>Female</td>
      <td>5/25/2006</td>
      <td>11:30 AM</td>
      <td>112238</td>
      <td>6.030</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>956</th>
      <td>Beverly</td>
      <td>Female</td>
      <td>10/17/1986</td>
      <td>12:51 AM</td>
      <td>80838</td>
      <td>8.115</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>604</th>
      <td>Bruce</td>
      <td>Male</td>
      <td>3/15/2013</td>
      <td>11:13 PM</td>
      <td>141335</td>
      <td>15.427</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>456</th>
      <td>Deborah</td>
      <td>NaN</td>
      <td>2/3/1983</td>
      <td>11:38 PM</td>
      <td>101457</td>
      <td>6.662</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>615</th>
      <td>Edward</td>
      <td>Male</td>
      <td>8/30/2001</td>
      <td>1:24 AM</td>
      <td>73105</td>
      <td>6.083</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>209</th>
      <td>Emily</td>
      <td>Female</td>
      <td>9/20/2007</td>
      <td>11:25 AM</td>
      <td>89434</td>
      <td>11.295</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>908</th>
      <td>Janice</td>
      <td>Female</td>
      <td>12/17/2009</td>
      <td>6:42 AM</td>
      <td>102697</td>
      <td>3.283</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>761</th>
      <td>Jennifer</td>
      <td>Female</td>
      <td>3/31/2015</td>
      <td>7:43 PM</td>
      <td>132084</td>
      <td>10.006</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>719</th>
      <td>John</td>
      <td>Male</td>
      <td>1/29/1999</td>
      <td>3:07 AM</td>
      <td>67165</td>
      <td>13.001</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>474</th>
      <td>Jonathan</td>
      <td>Male</td>
      <td>8/15/2002</td>
      <td>12:01 AM</td>
      <td>104749</td>
      <td>11.364</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>214</th>
      <td>Julie</td>
      <td>Female</td>
      <td>7/23/1989</td>
      <td>1:52 PM</td>
      <td>109588</td>
      <td>3.550</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>816</th>
      <td>Kelly</td>
      <td>Female</td>
      <td>3/17/2007</td>
      <td>6:20 PM</td>
      <td>39371</td>
      <td>4.068</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>558</th>
      <td>Linda</td>
      <td>Female</td>
      <td>8/18/1985</td>
      <td>4:34 AM</td>
      <td>51431</td>
      <td>13.295</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>191</th>
      <td>Lois</td>
      <td>Female</td>
      <td>10/18/2013</td>
      <td>4:51 PM</td>
      <td>36946</td>
      <td>6.652</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Nancy</td>
      <td>Female</td>
      <td>9/23/2000</td>
      <td>8:05 AM</td>
      <td>94976</td>
      <td>13.830</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>707</th>
      <td>Patricia</td>
      <td>Female</td>
      <td>3/7/1998</td>
      <td>1:10 AM</td>
      <td>75825</td>
      <td>7.839</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>551</th>
      <td>Philip</td>
      <td>Male</td>
      <td>7/18/1985</td>
      <td>6:36 AM</td>
      <td>122319</td>
      <td>19.122</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>632</th>
      <td>Rebecca</td>
      <td>Female</td>
      <td>2/23/1990</td>
      <td>3:21 PM</td>
      <td>134673</td>
      <td>6.878</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>402</th>
      <td>Richard</td>
      <td>NaN</td>
      <td>11/28/1992</td>
      <td>5:05 PM</td>
      <td>124655</td>
      <td>14.272</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>475</th>
      <td>Stephanie</td>
      <td>Female</td>
      <td>11/26/1992</td>
      <td>12:54 AM</td>
      <td>122121</td>
      <td>7.937</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>967</th>
      <td>Thomas</td>
      <td>Male</td>
      <td>3/12/2016</td>
      <td>3:10 PM</td>
      <td>105681</td>
      <td>19.572</td>
      <td>False</td>
      <td>Engineering</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Tina</td>
      <td>Female</td>
      <td>6/12/2009</td>
      <td>7:16 AM</td>
      <td>114767</td>
      <td>3.711</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
  </tbody>
</table>
</div>





    300    111786
    372     67827
    8       95570
    262     69134
    138    112238
    956     80838
    604    141335
    456    101457
    615     73105
    209     89434
    908    102697
    761    132084
    719     67165
    474    104749
    214    109588
    816     39371
    558     51431
    191     36946
    50      94976
    707     75825
    551    122319
    632    134673
    402    124655
    475    122121
    967    105681
    113    114767
    Name: Salary, dtype: int64




```python
display(group.max())
group.max('Salary')
```

    C:\Users\91896\AppData\Local\Temp\ipykernel_1900\3118248798.py:1: FutureWarning: Dropping invalid columns in DataFrameGroupBy.max is deprecated. In a future version, a TypeError will be raised. Before calling .max, select only columns which should be valid for the function.
      display(group.max())
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Start Date</th>
      <th>Last Login Time</th>
      <th>Salary</th>
      <th>Bonus %</th>
      <th>Senior Management</th>
    </tr>
    <tr>
      <th>Team</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Business Development</th>
      <td>9/8/1984</td>
      <td>9:40 PM</td>
      <td>140136</td>
      <td>19.626</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Client Services</th>
      <td>9/11/2002</td>
      <td>9:50 AM</td>
      <td>132839</td>
      <td>19.731</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Distribution</th>
      <td>9/2/1980</td>
      <td>9:16 PM</td>
      <td>135990</td>
      <td>19.908</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Engineering</th>
      <td>9/23/2000</td>
      <td>8:05 AM</td>
      <td>141335</td>
      <td>19.717</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Finance</th>
      <td>9/27/1995</td>
      <td>9:30 PM</td>
      <td>140850</td>
      <td>19.780</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Human Resources</th>
      <td>9/8/1994</td>
      <td>9:34 AM</td>
      <td>116931</td>
      <td>18.784</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Legal</th>
      <td>8/4/1993</td>
      <td>9:46 PM</td>
      <td>135882</td>
      <td>19.944</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Marketing</th>
      <td>9/3/1983</td>
      <td>9:19 AM</td>
      <td>146812</td>
      <td>18.674</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Product</th>
      <td>9/3/1997</td>
      <td>9:15 AM</td>
      <td>145274</td>
      <td>18.225</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Sales</th>
      <td>7/9/2011</td>
      <td>9:04 PM</td>
      <td>144887</td>
      <td>18.536</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Salary</th>
      <th>Bonus %</th>
    </tr>
    <tr>
      <th>Team</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Business Development</th>
      <td>140136</td>
      <td>19.626</td>
    </tr>
    <tr>
      <th>Client Services</th>
      <td>132839</td>
      <td>19.731</td>
    </tr>
    <tr>
      <th>Distribution</th>
      <td>135990</td>
      <td>19.908</td>
    </tr>
    <tr>
      <th>Engineering</th>
      <td>141335</td>
      <td>19.717</td>
    </tr>
    <tr>
      <th>Finance</th>
      <td>140850</td>
      <td>19.780</td>
    </tr>
    <tr>
      <th>Human Resources</th>
      <td>116931</td>
      <td>18.784</td>
    </tr>
    <tr>
      <th>Legal</th>
      <td>135882</td>
      <td>19.944</td>
    </tr>
    <tr>
      <th>Marketing</th>
      <td>146812</td>
      <td>18.674</td>
    </tr>
    <tr>
      <th>Product</th>
      <td>145274</td>
      <td>18.225</td>
    </tr>
    <tr>
      <th>Sales</th>
      <td>144887</td>
      <td>18.536</td>
    </tr>
  </tbody>
</table>
</div>




```python
em
g =em.groupby(['Team' , 'Gender'])['First Name'].count()
display(g)
g.to_csv('Team_Gender.csv')
g =pd.read_csv('Team_Gender.csv')
g # this is now convert into csv file.
```


    Team                  Gender
    Business Development  Female    16
                          Male       9
    Client Services       Female     8
                          Male       4
    Distribution          Female     7
                          Male      13
    Engineering           Female    16
                          Male       8
    Finance               Female     6
                          Male       5
    Human Resources       Female     6
                          Male       5
    Legal                 Female     5
                          Male      13
    Marketing             Female     6
                          Male       6
    Product               Female    12
                          Male      12
    Sales                 Female     7
                          Male      10
    Name: First Name, dtype: int64





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Team</th>
      <th>Gender</th>
      <th>First Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Business Development</td>
      <td>Female</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Business Development</td>
      <td>Male</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Client Services</td>
      <td>Female</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Client Services</td>
      <td>Male</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Distribution</td>
      <td>Female</td>
      <td>7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Distribution</td>
      <td>Male</td>
      <td>13</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Engineering</td>
      <td>Female</td>
      <td>16</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Engineering</td>
      <td>Male</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Finance</td>
      <td>Female</td>
      <td>6</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Finance</td>
      <td>Male</td>
      <td>5</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Human Resources</td>
      <td>Female</td>
      <td>6</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Human Resources</td>
      <td>Male</td>
      <td>5</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Legal</td>
      <td>Female</td>
      <td>5</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Legal</td>
      <td>Male</td>
      <td>13</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Marketing</td>
      <td>Female</td>
      <td>6</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Marketing</td>
      <td>Male</td>
      <td>6</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Product</td>
      <td>Female</td>
      <td>12</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Product</td>
      <td>Male</td>
      <td>12</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Sales</td>
      <td>Female</td>
      <td>7</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Sales</td>
      <td>Male</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python

emm = em[em['Team'] == 'Engineering']
display(emm[['Salary']].max())
display(em[em['Salary'] == emm['Salary'].max()])
display(em['Salary'].max())
display(em[em['Salary'] == em['Salary'].max()])
```


    Salary    141335
    dtype: int64



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Gender</th>
      <th>Start Date</th>
      <th>Last Login Time</th>
      <th>Salary</th>
      <th>Bonus %</th>
      <th>Senior Management</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>604</th>
      <td>Bruce</td>
      <td>Male</td>
      <td>3/15/2013</td>
      <td>11:13 PM</td>
      <td>141335</td>
      <td>15.427</td>
      <td>True</td>
      <td>Engineering</td>
    </tr>
  </tbody>
</table>
</div>



    146812



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Gender</th>
      <th>Start Date</th>
      <th>Last Login Time</th>
      <th>Salary</th>
      <th>Bonus %</th>
      <th>Senior Management</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>452</th>
      <td>Scott</td>
      <td>Male</td>
      <td>11/17/2012</td>
      <td>2:47 PM</td>
      <td>146812</td>
      <td>1.965</td>
      <td>True</td>
      <td>Marketing</td>
    </tr>
  </tbody>
</table>
</div>


<div style = "  display : flex; justify-content: center; ">
    <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
           Merging Concept
    </h1>
   
 </div>
  <p> 
    Pandas have options for high-performance in-memory merging and joining. When we need to combine very large DataFrames, joins serve as a powerful way to perform these operations swiftly. Joins can only be done on two DataFrames at a time, denoted as left and right tables. The key is the common column that the two DataFrames will be joined on. It’s a good practice to use keys which have unique values throughout the column to avoid unintended duplication of row values. Pandas provide a single function, merge(), as the entry point for all standard database join operations between DataFrame objects.
</p>


```python
data1 = {'key': ['k0', 'k1', 'k2'],
         'Name':['Jai', 'Princi','Anuj'], 
        'Age':[27, 24, 22],} 
data2 = {
    'key' : ['k0' , 'k1' , 'k2', 'k3'] ,
    'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
    'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']   
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
display(df1, df2)
# using .merge() function. 
res = pd.merge(df1,df2 , on='key' )
print( "\n" , 'Merging')
display(res)

```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>k0</td>
      <td>Jai</td>
      <td>27</td>
    </tr>
    <tr>
      <th>1</th>
      <td>k1</td>
      <td>Princi</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>k2</td>
      <td>Anuj</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>Address</th>
      <th>Qualification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>k0</td>
      <td>Nagpur</td>
      <td>Btech</td>
    </tr>
    <tr>
      <th>1</th>
      <td>k1</td>
      <td>Kanpur</td>
      <td>B.A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>k2</td>
      <td>Allahabad</td>
      <td>Bcom</td>
    </tr>
    <tr>
      <th>3</th>
      <td>k3</td>
      <td>Kannuaj</td>
      <td>B.hons</td>
    </tr>
  </tbody>
</table>
</div>


    
     Merging
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>Name</th>
      <th>Age</th>
      <th>Address</th>
      <th>Qualification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>k0</td>
      <td>Jai</td>
      <td>27</td>
      <td>Nagpur</td>
      <td>Btech</td>
    </tr>
    <tr>
      <th>1</th>
      <td>k1</td>
      <td>Princi</td>
      <td>24</td>
      <td>Kanpur</td>
      <td>B.A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>k2</td>
      <td>Anuj</td>
      <td>22</td>
      <td>Allahabad</td>
      <td>Bcom</td>
    </tr>
  </tbody>
</table>
</div>



```python
# how is methodology and inner is default (analysis with above) ,            
display(pd.merge(df1 , df2 , on='key' , how='inner'))
display(pd.merge(df1 , df2 , on='key' , how='outer'))
display(pd.merge(df1 , df2 , on='key' , how='right'))
display(pd.merge(df1 , df2 , on='key' , how='left'))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>Name</th>
      <th>Age</th>
      <th>Address</th>
      <th>Qualification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>k0</td>
      <td>Jai</td>
      <td>27</td>
      <td>Nagpur</td>
      <td>Btech</td>
    </tr>
    <tr>
      <th>1</th>
      <td>k1</td>
      <td>Princi</td>
      <td>24</td>
      <td>Kanpur</td>
      <td>B.A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>k2</td>
      <td>Anuj</td>
      <td>22</td>
      <td>Allahabad</td>
      <td>Bcom</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>Name</th>
      <th>Age</th>
      <th>Address</th>
      <th>Qualification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>k0</td>
      <td>Jai</td>
      <td>27.0</td>
      <td>Nagpur</td>
      <td>Btech</td>
    </tr>
    <tr>
      <th>1</th>
      <td>k1</td>
      <td>Princi</td>
      <td>24.0</td>
      <td>Kanpur</td>
      <td>B.A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>k2</td>
      <td>Anuj</td>
      <td>22.0</td>
      <td>Allahabad</td>
      <td>Bcom</td>
    </tr>
    <tr>
      <th>3</th>
      <td>k3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Kannuaj</td>
      <td>B.hons</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>Name</th>
      <th>Age</th>
      <th>Address</th>
      <th>Qualification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>k0</td>
      <td>Jai</td>
      <td>27.0</td>
      <td>Nagpur</td>
      <td>Btech</td>
    </tr>
    <tr>
      <th>1</th>
      <td>k1</td>
      <td>Princi</td>
      <td>24.0</td>
      <td>Kanpur</td>
      <td>B.A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>k2</td>
      <td>Anuj</td>
      <td>22.0</td>
      <td>Allahabad</td>
      <td>Bcom</td>
    </tr>
    <tr>
      <th>3</th>
      <td>k3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Kannuaj</td>
      <td>B.hons</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>Name</th>
      <th>Age</th>
      <th>Address</th>
      <th>Qualification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>k0</td>
      <td>Jai</td>
      <td>27</td>
      <td>Nagpur</td>
      <td>Btech</td>
    </tr>
    <tr>
      <th>1</th>
      <td>k1</td>
      <td>Princi</td>
      <td>24</td>
      <td>Kanpur</td>
      <td>B.A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>k2</td>
      <td>Anuj</td>
      <td>22</td>
      <td>Allahabad</td>
      <td>Bcom</td>
    </tr>
  </tbody>
</table>
</div>


![image.png](attachment:image.png)

## Transform Name(Mapping)


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>Address</th>
      <th>Qualification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>k0</td>
      <td>Nagpur</td>
      <td>Btech</td>
    </tr>
    <tr>
      <th>1</th>
      <td>k1</td>
      <td>Kanpur</td>
      <td>B.A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>k2</td>
      <td>Allahabad</td>
      <td>Bcom</td>
    </tr>
    <tr>
      <th>3</th>
      <td>k3</td>
      <td>Kannuaj</td>
      <td>B.hons</td>
    </tr>
  </tbody>
</table>
</div>




```python
#  I want to transform the address name in shortcut 
#  create Dictionary 
mapping = {'Nagppur':'NG' , 'Kanpur' : 'CNB'  , 'Allahabad' : 'PRG' ,'Kannuaj' :'KJN'}
df2['Address'].map(mapping)

```




    0    NaN
    1    CNB
    2    PRG
    3    KJN
    Name: Address, dtype: object




```python
df2['Address'] = df2['Address'].map(mapping)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>Address</th>
      <th>Qualification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>k0</td>
      <td>NaN</td>
      <td>Btech</td>
    </tr>
    <tr>
      <th>1</th>
      <td>k1</td>
      <td>CNB</td>
      <td>B.A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>k2</td>
      <td>PRG</td>
      <td>Bcom</td>
    </tr>
    <tr>
      <th>3</th>
      <td>k3</td>
      <td>KJN</td>
      <td>B.hons</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
