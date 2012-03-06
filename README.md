Python's Natural Language Toolkit Helper functions for text stemming, tagging and comparing.

Ussage is simple, import the library:

    from nltk_helper import *

To stem a piece of text:

    get_stems('The Wall Street Journal previously reported that AT&T and Verizon would be getting LTE-equipped iPads, but had no word on carriers outside the U.S.')
    
    >>> ['carrier', 'equip', 'get', 'ipad', 'journal', 'lte', 'outsid', 'previous', 'report', 'street', 'verizon', 'wall', 'word']

To tag a piece of text:

    get_tags('The Wall Street Journal previously reported that AT&T and Verizon would be getting LTE-equipped iPads, but had no word on carriers outside the U.S.')
    
    >>> [('AT', None), ('Verizon', None), ('LTE', None), ('iPads', None), (',', ','), ('.', '.'), ('.', '.'), ('The', 'AT'), ('no', 'AT'), ('the', 'AT'), ('be', 'BE'), ('and', 'CC'), ('but', 'CC'), ('&', 'CC-TL'), ('that', 'CS'), ('had', 'HVD'), ('-', 'IN'), ('on', 'IN'), ('outside', 'IN'), ('would', 'MD'), ('word', 'NN'), ('Wall', 'NN-TL'), ('Street', 'NN-TL'), ('Journal', 'NN-TL'), ('carriers', 'NNS'), ('T', 'NP'), ('U', 'NP'), ('S', 'NP'), ('previously', 'RB'), ('getting', 'VBG'), ('reported', 'VBN'), ('equipped', 'VBN')]

To compare two pieces of text:
    
    t1 = """iPad 3 will have 4G LTE networking - The same source that originally told iMore Apple would be holding their iPad 3 event on March 7 has now let us know that the announcement will include 4G LTE networking. We’d heard previously that 4G LTE would be coming to iOS in 2012, but not whether it would make the cut for iPad 3, or whether Apple would save it for iPhone 5 in October.  Sounds like LTE is good to go, though it remains to be seen how Apple will handle the many different 4G bands being used internationally. The Wall Street Journal previously reported that AT&T and Verizon would be getting LTE-equipped iPads, but had no word on carriers outside the U.S.  Verizon has the most to gain from an LTE iPad. Right now, Verizon is stuck carrying an iPad 2 that gets up to 3mbps on EVDO Rev. A, well below the theoretical 14.4mbps offered on AT&T’s HSPA network. Given how far ahead Verizon is with LTE, that has to sting, as has to be something they want Apple to address.  Despite recent uncertainty about the process, iMore is also still hearing that the iPad 3 will ship with a quad-core processor. We’ll find out one way or another on Wednesday.  For a complete rundown of all the rumors, check out our iPad 3 event preview or jump into our iPad 3 Forums."""
    
    t2 = """iPad 3 set to launch with 4G LTE: Expect an iPhone version? - Citing the same source that informed iMore of the March 7th announcement date of Apple’s latest tablet, it is believed that the upcoming iPad will launch with 4G LTE technology.  It’s not the first time the claim has been made. But as the launch comes closer with only two days until chief executive Tim Cook takes the stage for his first major product announcement, historically this is the week where the tidbits of semi-accurate leaks hit the media.  The only thing we really know is what Apple is telling us. We know there is something set for two days time, and we expect it to be an iPad announcement. The claim: “The same source that originally told iMore Apple would be holding their iPad 3 event on March 7 has now let us know that the announcement will include 4G LTE networking.”  Sounds like LTE is good to go, though it remains to be seen how Apple will handle the many different 4G bands being used internationally. The Wall Street Journal previously reported that AT&T and Verizon would be getting LTE-equipped iPads, but had no word on carriers outside the U.S.”  Call me skeptical, but it could go either way. There are three things that spring to mind: Battery technology is still not to the point where devices like the iPad or iPhone can be made their intended slim size, and not forfeit a battery that is wholly compatible with 4G LTE. The high-speed networking requires a larger battery for the same usage hours as a 3G phone. It’s why you see so many phones with battery extender packs.  Apple doesn’t do ‘developing’ in that it takes on technologies it knows consumers will use. 4G LTE is still growing and on a worldwide level is still slim. NFC — and even 4G at the time, to some extent — was thought to be the next great thing and yet it was left out of the iPhone 4S launch completely.  Verizon would benefit (and suffer) because Apple does play favourite, and not just in its media reporting of who gets what. Verizon would benefit massively from a 4G tablet as it is the only U.S. network to currently stock the iPad. But Verizon must have known for a great deal of time as part of its inevitable efforts to prepare its still-developing next-generation network that a 4G tablet was on its way. On the other side of the pond, while joint venture Everything Everywhere, made up from Orange UK and T-Mobile UK, is soon to bring out a 4G LTE network in the region, Europe is practically bone dry in terms of 4G connectivity. Apple won’t bring out an iPad just for 4G markets, nor can it afford to bring out 4G to markets that have years until 4G spectrum is divvied up rolled out — years in which the company could be spending on developing better battery technologies. The case of precedence will also ring some bells. Does an iPad with 4G technology mean that the next iteration of the iPhone will too? Will the iPhone 5 be thicker? Or will it have a removable back for a battery extender? Throwing out one question throws back no answers, yet even more questions. At this stage, it would be pointless to speculate.  Only two days to wait, and all shall be revealed. ZDNet and sister-site CNET will be reporting as the announcement happens."""
    
    compare(txt1=t1, txt2=t2)
    
    >>> True
    
    get_comp_rate(txt1=t1, txt2=t2)
    
    >>> 49.39759036144578

txt1 and txt2 from these articles:

* http://www.imore.com/2012/03/05/ipad-3-4g-lte-networking/

* http://www.zdnet.com/blog/btl/ipad-3-set-to-launch-with-4g-lte-expect-an-iphone-version/70833

Which are clearly related.

You should be able to pinpoint the exact point of "relatedness" by moving around the threshold in the get_th() function.  By default it's set to 35%, but could be variable depending on your needs.