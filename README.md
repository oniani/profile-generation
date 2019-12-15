# Profile Generator

[A demonstration of a simple, on-the-fly user profile generation:
http://profile-generator.herokuapp.com](http://profile-generation.herokuapp.com)

The API is available (here)[http://profile-generation.herokuapp.com/api].

![Generated Profile](./demo/generated-profile.png)

## Running

Make sure to have [Python](https://www.python.org/) installed and run the
following commands in the order specified below.

```{sh}
git clone https://github.com/oniani/profile-generation.git
cd profile-generation
python3 -m pip install -r requirements.txt
flask run
```

After running the commands above, open localhost (usually, port 5000) in the
browser and refresh the page. If everything to this point worked well, the app
should generate a new profile on every refresh of the page.

## References

- [This Person Does Not Exist](https://thispersondoesnotexist.com/)
- [textgenrnn](https://github.com/minimaxir/textgenrnn)
- [names](https://github.com/treyhunner/names)

## License

[GNU General Public License v3.0](LICENSE)
