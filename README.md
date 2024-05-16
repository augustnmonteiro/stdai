### STDAI

Simple tool to help you debug your terminal errors.
![A GIF showing STDAI working](https://github.com/augustnmonteiro/stdai/blob/main/stdai.gif?raw=true "A GIF showing STDAI working")

## Requirements
- [Ollama](https://ollama.com/)
- Python

## Usage
1. Clone the repository
2. Start the stdai.py in one terminal
3. Run `./run.sh <your command>` in another terminal

## Example
```bash
./run.sh node index.js
```
or 
```bash
./run.sh python3 main.py
```

## To make it easier you can add an alias to your .bashrc or .zshrc
> Run the following command in the terminal inside the stdai directory
> This will generate an alias for your then
> Copy the output and paste it in your .bashrc or .zshrc
```bash
echo "alias stdai=\"$(pwd)/run.sh\""
```

## Roadmap
- [ ] Chat in the terminal keeping the context of the error 
- [ ] Support to other LLMs
  - [ ] ChatGPT
  - [ ] Gemini
  - [x] LLama
- [ ] Support tools like `nodemon` 
- [ ] Pretty/Formatted/Fancy output 
- [ ] Quick fix suggestions
- [ ] Chat commands
  - [ ] `/clear` to clear the chat
  - [ ] `/exit` to exit the chat
  - [ ] `/help` to get help
  - [ ] `/c` to copy the error message
  - [ ] `cf` to copy quick fix if available
- [ ] Notifications for new errors so you don't have to keep checking the terminal
- [ ] Install script
  
## Contributing
Feel free to contribute to this project. 

## License
MIT License