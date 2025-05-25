🚀 **Blast from the Past: My First MNIST CNN Adventure!** 🚀

Yo! Check out this project – it’s a throwback to when I first dove into building Convolutional Neural Networks, trying to teach a computer to read MNIST digits. It’s pretty wild to see my early thought process in action! 😅 It *kinda* managed to recognize the three digits I fed it ('2', '3', '5'), but looking back, there are definitely some "learning opportunities" (aka, lovable oopsies!) and things I'd totally rock differently today.

Here's the lowdown on the charming quirks:

* 🧠 **Prediction Brain Fart:** When the model tried to spot a '5', it was on a wild goose chase looking for `predicted_label == 4`. My own `label_map = {0: 2, 1: 3, 2: 5}` clearly shows that was a bit of a mix-up! Should've been `predicted_label == 5`. Classic!

* 🌈 **Color Me Confused (on Grayscale!):** I built the model expecting full-color, 3-channel images (`input_shape=(28,28,3)`). Plot twist: MNIST is famously **grayscale**! A simpler 1-channel setup (`(28,28,1)`) would have been the slicker, more sensible move.

* 📐 **The Great Resizing Rumba:** For new images, I had them doing this bizarre dance – blowing up to `(256,256)` pixels, only to shrink right back down to `(28,28)`. Talk about an unnecessary detour! Going straight to `(28,28)` would've been cleaner and probably kept the digits looking sharper.

Seriously though, revisiting this old code is a blast. It's awesome to see how far my skills have leveled up since these early experiments. 📈 Super stoked about the progress and excited for what's next! ✨
