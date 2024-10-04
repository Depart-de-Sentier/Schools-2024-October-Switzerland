# October 2024 School on Advanced Inventory Modelling

> [!IMPORTANT]
> 🙋‍♀️🙋‍♂️ School Chat Room \
> [Join the chat Get help from team coaches and other students here!](https://matrix.to/#/#dds-schools:matrix.org) \

# Logistics

The course will start with lunch on Sunday, Oct. 6, at 12:00 in the Möschberg Seminar Hotel in Grosshöchstten. We recommend arriving on the 11:04 train (see https://www.sbb.ch/; the train station is "Grosshöchstten"), and the hotel will meet us to carry us (or at least our luggage) up the hill to the hotel, which is just outside the village. I will will walk up and would be happy to guide anyone who wants to come on foot as well, as long as the weather cooperates.

The school officially ends on Friday at 16:00, but we offer an Apéro with drinks and light snacks from 16:00 to late on Friday evening. Please note that you need to make individual arrangements with the hotel if you want to stay on Friday evening, or arrive early on Saturday.

You will need a computer. Note that [Swiss plugs](https://en.wikipedia.org/wiki/SN_441011) are [just different enough](https://www.reddit.com/r/Switzerland/comments/1vxw41/comment/cewuhca/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) from other EU plugs to be annoying - we will bring a few adapters, but try to sort this out on your own if possible.

# Room and Board

[Möschberg](https://moeschberg.ch/) was originally set up as an educational center for farmers who wanted to learn about organic agriculture. It is plain but pleasant, with a lot of common space, gardens, and easy access to hiking paths. Bathrooms and showers are shared, so please bring what you need to be comfortable (towels are provided).

The food is cooked by the kitchen staff on site, and there is a lot of it. Lunch is usually two courses, and dinner three courses. There will always be a vegan option available, and we have asked them to limit the number of days with meat consumption. We have also told them about your food allergies or restrictions.

If you are in a shared room, there will be two single beds separated from each by around one meter. There are wardrobes and desks in the rooms, and all rooms have outside windows.

# School content

This course is on "inventory modelling at scale." What does that mean? If we think about the demands being put on life cycle assessment, and contrast that with the time and money it takes to produce an ISO-compliant LCA, it is clear that something needs to change. Our hypothesis is that we can improve both the quality and quantity of inventory data by changing the way we generate inventories. To do this we need to solve three fundamental problems:

* How do I find the specific data I'm looking for?
* How do I maintain data, or bring data up to current conditions?
* How do I adapt the data I've found for my specific use case?

To be very blunt, we don't think that these problems can be solved with standard unit processes development. Instead, we need a set of components which, when assembled together, can generate background and foreground data at a level of scientific quality not present in current LCA practice.

The first component is a common taxonomy and vocabulary which understands the LCA world but locates it in a broader context. There's no need to reinvent wheels here - we have international systems used to label processes, goods, units, places, etc. We are building this common vocabulary at [vocab.sentier.dev](https://vocab.sentier.dev/en-US/), and will continue to improve it in preparation for the school.

This first component can solve the search problem, or at least solve it enough for now. See the bottom of [the "KiloGM" vocab page](https://vocab.sentier.dev/qudt/en-US/page/?clang=en&uri=https%3A%2F%2Fvocab.sentier.dev%2Fqudt%2Funit%2FKiloGM) to see how our vocabulary can include concepts from other systems, and describe what those relationships look like.

To make systems maintainable, we can start by thinking about what changes over time, and what doesn't. The fundamental equations or logic in production systems don't change - rather, it's the numbers which change. Let's split these two concepts so that we have models and numerical data as two separate objects, which can be stored and managed separately. Models are computational objects that describe our understanding of how our systems work, based on first principles, experimental data, simulations, etc. We probably won't be so lucky that our models are just a few simple equations, but in our experience even complicated Excel models can be split into smaller functions without too much pain.

What does data look like? One important step beyond current standard practice is to think of each input parameter as a vector of possible values instead of a single coefficient. The values themselves can come from many places, but in the work we have done so far it is quite normal to find actual datasets when you start looking for them. You can think of the data vectors are being fancy Numpy arrays, attached to a spatiotemporal context and representing a term from the shared taxonomy.

The data can then feed into the models, and models should produce one or more output data vectors. One important element in this feeding process is that we are using a hierarchical taxonomy, so models can ask for one level of aggregation, and data at another level can be fed into the system (e.g. I need cheese but get data for specific cheese varieties). It's up to us to figure out how to interpolate data across these scales, and there will be a lot of fun data science here ;) We do want to emphasize that we want the data to make decisions whenever possible (in contrast to the large amount of practitioner judgment used in LCA right now). Once we have larger result sets we can feed these into various algorithms, and pick the simplest or most elegant one which produces high quality results.

In this paradigm, we get maintainability - you just upload the new CSV of last years values, and the continuous integration system will analyze what changed, why it changed, and give you a report. You also get flexibility because you can filter out data feeding into the model, so the same data and models can calculate the eutrophication impact of global average chees and Appenzeller.

We will be writing these components during the school itself, and appreciate your patience and understanding in advance - not everything will work perfectly!

We have had several retreats discussing these ideas; you can find some discussions at the [sentier.dev Github repo](https://github.com/sentier-dev/sentier.dev/).

# Schedule

The schedule will be adapted during the course - the following is a rough outline.

## Sunday afternoon

* 13:30 Welcome and introduction
* 14:30 Input lecture on Sentier.dev initiative (Mutel)
* 15:00 Models (Mutel)
* 17:00 Group formation (Navarrete)
* 18:30 Dinner
* 20:00 Effective use of git and Github (Guimaraes)

## Monday morning

* 8:00 Breakfast
* 9:00 Semantic vocabularies (Mutel)
* 10:30 Harmonizing and storing data (Mutel)
* 12:00 Lunch

## Monday afternoon

* 13:30 Using the Python library template (Navarrete)
* 14:00 HESTIA models (Royer)
* 15:00 Documentation (Weinold)
* 15:30 Logging (Navarrete)
* 16:00 Testing (Guimaraes)
* 16:30 Development exercise
* 18:30 Dinner
* 20:00 Development exercise continued

## Tuesday morning

* 9:00 Brightway refresher and best practices (Mutel)
* 11:00 Group work

## Tuesday afternoon - Friday morning

* Group work interspersed with short input lectures (TBD)

## Friday afternoon

* 14:00 Group presentations
* 15:15 Course review and feedback
* 15:45 Next steps
* 16:00 Apéro

# Group work

This course is organized around group projects.

There are around 26 students and 4 instructors at the school, but many of the "students" are very experienced. In the group formation, we will try to make groups with a good mix of background knowledge and programming expertise. We would like to have groups of between 4 and 6 people, and the instructors will be supporting the groups and sitting with them most of the time.

Group work is not graded. But we would like you to produce useful outputs which can help the platform in the future, so we will be guiding group themes, and it's much more useful to do one thing right than do a lot of things halfway.

# Preparation

To prepare for the course, please do the following (all important, but in order of priority):

* Please prepare a single slide introducing yourself, and upload it to [Google Docs](https://docs.google.com/presentation/d/18Nzb5XAeXLiEAcn592dm72bRy3lHH5WRk6lpdmKlYr0/edit?usp=sharing). To get the layout perfect we recommend uploading a screenshot or PDF.
* Identify one model which could be adopted with the school timeframe. It doesn't have to be an LCA model, but should be helpful for industrial ecology. It can be simple or complex (if you understand them, we can probably build them quickly). Be prepared to *present it verbally*.
* Search for a standard catalogue of terms needed for your model. This could be from a standardization organization, e.g. ISO, DIN, ANSI, or from an industry catalogue, or a well-maintained ontology or taxonomy which we can use (like [ChEBI](https://www.ebi.ac.uk/chebi/)).
* Practice your Python. You should understand simple data types, what a function is, what a class is, and the basics of type annotation.
* If you want to do some preparatory reading, you can look at [SKOS primer](https://www.w3.org/TR/skos-primer/).
