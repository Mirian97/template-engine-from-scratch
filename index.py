from Templite import Templite

# Make a Templite object.
templite = Templite('''
    <h1>Hello {{name|upper}}!</h1>
    {% for topic in topics %}
        <p>You are interested in {{topic}}.</p>
    {% endfor %}
    ''',
    {'upper': str.upper},
)

text = templite.render({
    'name': "Mirian",
    'topics': ['Python', 'Java', 'Watercolor', 'Amigurumi'],
})

print(text)