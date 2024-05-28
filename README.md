# sose24-projekt-LLMs
University project for the class "Wie konkurrenzfähig sind Open LLMs? " of the SoSe24

## Goal:

- Compare different text-to-image Opensource Models in their capacity of creating accurate monsters from the dungeon and dragons universum (using the monster manual as description basis).

### Example: DEVA
*"Devas are angels that act as divine messengers or
agents to the Material P lane, the Shadowfell, and the
Feywild and that can assume a form appropriate to the
realm they are sent to.
Legend tells of angels that take mortal form for years,
lending aid, hope, and courage to good hearted folk. A
deva can take any shape, although it prefers to appear
to mortals as an innocuous humanoid or animal. When
circumstances require that it cast off its guise, a deva is
a beautiful humanoid-like creature with silvery skin. Its
hair and eyes gleam with an unearthly luster, and large
feathery wings unfurl from its shoulder blades."*

-->According to this description, a model should be able to produce an image in a similar style than the one provided before.

**Databank:** The official Monster Manual descriptions from Dungeon and Dragons (copyrights?, PDF? Or book) in english.

**OpenLLMs to test:** Still looking, maybe add a closed-llm for comparison? 

## Steps:

1) Collect all the descriptions from the Monster Manual (Hopefully works with an app/or code can be made)
2) Give the descriptions to the different models (Choose/randomize which ones to give)
- Informations to give: Monster name, monster description, art style in which to produce the art, required modifications when needed
3) Repeat the operation on the other models
4) Note the differences and the ease/speed with which the images were made
