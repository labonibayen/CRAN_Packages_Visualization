import pandas as pd
url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-11-12/loc_cran_packages.csv'
df = pd.read_csv(url)

list_languages = {"R":"R is a language and environment for statistical computing and graphics",
                  "HTML":"HTML (HyperText Markup Language) is the most basic building block of the Web. It defines the meaning and structure of web content.",
                  "CSS":"CSS stands for Cascading Style Sheet and it's a programming language used to define the style of a website together with HTML.",
                  "Python":"Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis.",
                  "JavaScript":"JavaScript is a dynamic programming language that's used for web development, in web applications, for game development, and lots more.",
                  "C++":"C++ is a cross-platform language that can be used to create high-performance applications."}

df_filtered = df[df['language'].isin(list_languages.keys())]

#proportionally shrink dataframe
sample_df = df_filtered.groupby('language', as_index=False).apply(lambda x: x.sample(frac=0.007)).reset_index()
sample_df.drop(columns=['level_0', 'level_1'], inplace=True)



# add the count to the original dataframe
grouped = sample_df.groupby('language')
count = grouped.size()
sample_df['count'] = grouped['language'].transform('size')

#format data for flask
df_trunc = sample_df[['language','pkg_name','count']]
df_trunc.insert(0, 'id', range(0, 0 + len(df_trunc)))

df_trunc["descriptions"] = df_trunc["language"]
df_trunc.replace({'descriptions':list_languages}, inplace=True)


df_trunc.to_csv("cran_data.csv")













