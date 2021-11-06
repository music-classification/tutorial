cd book
ghp-import -n -p -f _build/html
cd ..

# https://jupyterbook.org/start/publish.html
# To update your online book, make changes to your book’s content on the main branch of your repository, re-build your book with jupyter-book build mybookname/ and then use ghp-import -n -p -f mylocalbook/_build/html as before to push the newly built HTML to the gh-pages branch.
