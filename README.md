# sose24-projekt-LLMs
University project for the class "Wie konkurrenzfähig sind Open LLMs? " of the SoSe24

## Goal:

Compare different text-to-image Opensource Models in their capacity of creating accurate monsters from the dungeons and dragons universum (using the monster manual as description basis).

### Example:
**Deva** in hand-drawned style

*"Devas are [...] blades"*

-->According to this description, a model should be able to produce an image in a similar style than the one provided before.

-->Description hidden, copyrights

**Databank:** The official Monster Manual descriptions from Dungeon and Dragons (copyrights?, PDF? Or book) in english.

**OpenLLMs to test:**

- https://huggingface.co/runwayml/stable-diffusion-v1-5 (Most liked model)
- https://huggingface.co/ntc-ai/SDXL-LoRA-slider.dungeons-and-dragons-cover-artwork (model specifically for dungeons and dragons artwork)
(- Either closed-LLM (Dall-e/firefly) or https://huggingface.co/TheMistoAI/MistoLine (Top trending model) )

## Steps:

1) Collect all the descriptions from the Monster Manual (Hopefully works with an app/or code can be made)
2) Give the descriptions to the different models (Choose/randomize which ones to give)
- Informations to give: Monster name, monster description, art style in which to produce the art, required modifications when needed
3) Repeat the operation on the other models
4) Note the differences and the ease/speed with which the images were made

## What is analysed
- How well is the image reproduced from the description
- How fast was the image generated
- How many modifications were asked
- Is the art style respected across all generation?
- Can the model do well with the given description? Are the descriptions too vague? What needed to be changed in the original promt to get the desired result?
- *optional* Give the image to a image-to-text model and compare both descriptions
