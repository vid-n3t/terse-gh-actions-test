# github-practical-actions-4412872

## Personal Set up

```
# Clone the remote
git clone git@github.com:LinkedInLearning/github-practical-actions-4412872.git
# Create a branch
git checkout -b main-vid
# Rename origin to source
git remote origin source
# Remove push option from source to avoid accidental pushes
git remote set-url source --push ''
# Add your own fork or new repo
git remote add origin git@github.com:vid-n3t/terse-gh-actions-test.git
```

### Additional steps

1. Enable the git pre-commit hook
2. Instructions in the /scripts dir
3. Move site files to a \_sites/ dir so publishing doesn't include sensative files
