# The Valley Trading
Just under the Stardrop mountains, a young man named Mute lives out his dream as a traveling merchant.  And once he's done ferrying others' destinies, maybe he'll find his own.  Inspired by Spice and Wolf.

## Welcome!
This is a text based adventure trading game.  You travel between towns to peddle your wares, and there are plans to have quests/story elements.  Making contacts in each of the towns, learning their stories, and having new opportunities arise will from it will be the main gameplay loop.  I'll explain the structure of the code below.

## Contributions
These are welcome!  If anyone stumbles upon this little repository and wants to have a hand in the game's development, I'll do my best to be receptive!  Make an issue about what you're wanting to add if it isn't already listed.  Those will be the defacto roadmap.

### Code Structure
#### Main:
- Inserts data generated in initial_generation.py into variables.  Game data will then be stored in these variables for the rest of the game.
- Runs startup sequence of text when first running the game.
- Houses the main loop where all other functions are run from.  The default options you can choose in each city are housed in this loop in the form of functions.

#### Initial_Generation:
- Houses ITEM_WEIGHTS and ROAD_LENGTHS constants.  Road lengths are represented as the quantity of supplies required to travel between cities.
- Houses Player and Wagon functions which create dictionaries for these entities.  The dictionaries are stored in variables in Main.
- Houses functions that generate intial data for the cities.  This includes supply, base_price, and later moving_price (although this value is calculated later.)  This also loads the text that appears when a city is visited from a .csv file into a list that is randomly pulled from.

#### Running_Functions:
- Houses functions that are used in multiple files.

#### Market_Functions:
- Houses functions that are used when player visits the market.  Purchasing mechanics and change mechanics.  
- The moving_price variable which is stored in the city dictionaries is the current price of each good.  It is calculated based off the supply in all cities.  It's simple right now, but ``` base price * city supply / (supply of all cities) = moving price ```.  These creates some semblence of supply and demand, but much tweaking is required.  Supply and base price will remain the core ways to change the moving price, but I'm open to all sorts of ways to change those values.

#### Exchange_Functions:
- Houses functions that allow the player to exchange one denomination of currency for another.  Gold, silver, and copper all have weight and will all cost a fee to convert between.  Right now 1 gold = 10 silver = 1000 copper.
- You'll get change from merchants, but you must choose which denomination to pay in.

#### Travel_Functions:
- Houses functions that allow travel between cities.  Right now the map is hardcoded into these functions.  Each city is a node that can only reach other nodes.  I'm not sure how to make this more efficient, but a map is built for now and expanding it is a tedious, but understandable process.  Create the connecting nodes and initialize the city dictionary.  cities_idx in main will have to be updated as well.

#### Filler_Text.csv
- Houses city introduction text upon arriving in a new settlement.  It is randomly chosen.  Other messages that occur on the road or in specific dialogue will also be stored in .csv's like this.

#### The Valley Trading City Balancer
- Is a tool to balance supply levels in cities (unfinished)

#### Planning.txt
- The ramblings of a madman.
