سلام، در این درسنامه قرار هست تا درباره تعریف، ویژگی ها، مزایا
و معایب و همینطور کاربرد های توابع بی نام یا anonymous functions صحبت کنیم پس
کمربندهایتان را محکم ببندید 😊

## **تابع بی نام یا `Anonymous function` چیست؟**

تابع بی نام که به عنوان تابع لامبدا `lambda` نیز شناخته می شود، تابعی است که بدون نام در یک زبان برنامه نویسی تعریف می شود. به جای اینکه با یک شناسه استاندارد اعلان شود، یک تابع بی نام معمولاً برای یک هدف کوتاه مدت یا به عنوان یک آرگومان برای یک تابع مرتبه بالاتر تعریف و استفاده می شود.

## **توابع بی نام در پایتون:**

در پایتون در حالت عادی برای  تعریف توابع از کلمه کلیدی **`def`**  استفاده می شود. تابع در پایتون از چهار بخش تشکیل می شود:

1. **نام تابع**
2. **ورودی**
3. **عملیات**
4. **خروجی**

### مثال:
```python
def <mark title="نام تابع">add</mark>(<mark title="ورودی">a</mark>):
    <mark title="عملیات">c = a + a</mark>
    <mark title="خروجی">return c</mark> 
```

ماوس خود را روی قسمت‌های مختلف این تابع نگه‌دارید تا هر بخش را به خوبی بشناسید.

## تابع Lambda در پایتون

در پایتون برای تعریف توابع بی نام از کلمه کلیدی **`lambda`** استفاده می‌کنیم. تعریف یک تابع `lambda` در پایتون بسیار مختصرتر و شاید ساده‌تر از تابع معمولی آن است. کافی است از ساختار آن اطلاع کافی داشته باشید. یک تابع `lambda` از سه بخش تشکیل شده است:

1. **کلمه کلیدی `keyword`**
2. **ورودی `arguments`** 
3. **بدنه و عملیات `expression`**

تصویر زیر به خوبی ساختار یک تابع **`lambda`** را توضیح می‌دهد:
![](https://media.licdn.com/dms/image/D5612AQEWA8B4FZQqow/article-cover_image-shrink_720_1280/0/1680531889201?e=2147483647&v=beta&t=1RkKmWxrNoYOHdn-goUOeIUkq_SCqvNLGl5J1UzIGoc)


 ### یک مثال دیگر:
```python
<mark title="شی از تابع">multiply</mark> = <mark title="کلمه کلیدی" class="yellow">lambda</mark> <mark title="ورودی  ها">x, y, z</mark>: <mark title="بدنه  و عملیات">x * y * z</mark>
```


## **اصلا چرا باید از توابع بی نام استفاده کنیم؟**

1.  **مختصر و مفید بودن:**
	توابع لامبدا به شما این امکان را می‌دهند که در مقایسه با توابع معمولی و سنتی، کد کوتاه‌تر و مختصرتری بنویسید. به عنوان مثال:

```python
# تابع سنتی
def square(x):
	return x ** 2

# همان تابع با استفاده از لامبدا ولی کوتاه تر
square_lambda = lambda x: x ** 2
```

2. **ورودی به توابع دیگر به عنوان آرگومان**:
زمانی که نیاز است تا یک تابع را به عنوان آرگومان به یک تابع دیگر ورودی دهیم، توابع لامبدا به کمک ما می آیند. مثال:

```python
def operate(func, x, y):
	return func(x, y)

add = lambda x, y: x + y
result = operate(add, 5, 3)
```

در مثال بالا یک تابع با نام `operate` تعریف شده که دو متغییر و یک تابع را در ورودی به عنوان آرگومان دریافت می کند. در ادامه یک شی از تابع لامبدا تعریف کرده که دو متغییر `x`و`y` را دریافت و باهم جمع می کند. در نهایت این تابع را به عنوان ورودی به تابع بالاتر یعنی `operate` می دهیم تا از آن استفاده کند.
 
4. **برنامه نویسی کاربردی `functional`:**
توابع لامبدا به خوبی با مفاهیم برنامه نویسی کاربردی هماهنگ هستند و عملیات هایی مانند؛ مپ کردن`mapping`، فیلتر کردن`filtering`، مرتب سازی`sorting`و... را برای ما راحت تر میکنند. در باره نحوه کاربرد توابع لامبدا در این عملیات ها و مثال های آنها در قسمت بعد صحبت خواهیم کرد.

## **انواع کابرد تابع لامبدا و نحوه استفاده از آن:**

1. **استفاده در توابعی مانند `map` و `filter`:** 

###  مثال:

```python
numbers = [1, 2, 3, 4]

# Using lambda in map
squared = list(map(lambda x: x ** 2, numbers))

# Using lambda in the filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

در این مثال، تابع لامبدا برای محاسبه مربع اعداد در `map` و انتخاب اعداد زوج در `filter` استفاده شده است.

2. **مرتب سازی:**

### مثال: 	

```python
students = [('Alice', 25), ('Bob', 30), ('Charlie', 22)]

# مرتب‌سازی دانش‌آموزان بر اساس سن
sorted_students = sorted(students, key=lambda x: x[1])

data = {'apple': 5, 'orange': 2, 'banana': 8}

# مرتب‌سازی دیکشنری بر اساس مقدار
sorted_data = sorted(data.items(), key=lambda x: x[1])
```

در این مثال، تابع لامبدا به عنوان تابع کلید در توابع `sorted` برای مرتب‌سازی دانش‌آموزان بر اساس سن و مرتب‌سازی دیکشنری بر اساس مقدار انتخاب شده است. 

<details class="orange">
<summary>**نکته مهم**</summary>
### **چه مواقعی بهتر است از توابع لامبدا استفاده نکنیم؟**

شاید این سوال در ذهن شما شکل بگیرد که محدودیت ها و نباید ها در هنگام استفاده از توابع لامبدا چگونه است. در جواب این سوال باید به چند نکته توجه کرد. با این که توابع لامبدا روشی مناسب برای نوشتن توابع کوتاه و ساده هستند، اما یکی از محدودیت‌های اصلی آنها این است که به یک عبارت محدود می‌شوند، به این معنی که نمی‌توانند شامل چند دستور یا عبارت پیچیده باشند.

محدودیت دیگر این است که توابع لامبدا نام ندارند، که می‌تواند اشکال زدایی و درک کد را دشوارتر کند.به طور کلی، بهتر است از توابع نامگذاری شده برای **عملیات پیچیده** استفاده کنید و فقط از توابع لامبدا برای عملیات کوتاه و ساده استفاده کنید.
</details>
