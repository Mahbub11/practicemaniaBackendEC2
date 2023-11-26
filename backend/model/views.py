# from django.shortcuts import render
# from rest_framework.response import Response
# from django.http import JsonResponse,HttpResponse
# from rest_framework.decorators import api_view
# from typing import Union
# from gramformer import Gramformer
# import re
# import warnings
# from collections import defaultdict



# # ResultsType = dict[str, Union[str, list[Match]]]

# # Create your views here.
# gf = Gramformer(models=1, use_gpu=False) #1=corrector, 2=detector









# @api_view(["POST"])
# def checkSentenceGrammar(request, *args,**kwargs):
#     #  is_bad_rule = lambda rule: rule.message == 'Possible spelling mistake found.' and len(rule.replacements) and rule.replacements[0][0].isupper()
#     #  tool = language_tool_python.LanguageTool('en-US')
#     #  matches = tool.check(request.data['text'])
#     #  matches = [rule for rule in matches if not is_bad_rule(rule)]
#     #  result=language_tool_python.utils.correct(request.data['text'], matches)
#     # grammar_detector = GrammarDetector()
#     # results = grammar_detector(request.data['text'])
#     # tool = language_tool_python.LanguageTool('en-US')  # use a local server
#     # # tool = language_tool_python.LanguageTool('en-US', config={'maxSpellingSuggestions': 1})# or use public API
#     # results=tool.check(request.data['text'])
#     # gh= GrammarHelper()
#     # results=gh.polish(request.data['text'])
#     # return Response({'result':results})
#     Orders = [];
#     myDict = defaultdict(list)
#     req_data=request.data['influent_sentences']
#     for i, influent_sentence in enumerate(req_data):
#         corrected_sentences = gf.correct(influent_sentence, max_candidates=1)
#         for corrected_sentence in corrected_sentences:
#         #  Orders.append(gf.get_edits(influent_sentence, corrected_sentence))
#         #  myDict[i].append(gf.get_edits(influent_sentence, corrected_sentence))
#            Orders.append({i:gf.get_edits(influent_sentence, corrected_sentence),
#                           'correct':corrected_sentence})
#     return Response({'result':Orders})
    
#         # for corrected_sentence in corrected_sentences:
#         #  results1=gf.highlight(influent_sentence, corrected_sentence)
#         #  return Response({'result':results1})


#     # raw_Data=request.data['speech']
#     # results1=gf.correct(raw_Data)
#     # # results= gf.highlight(raw_Data,results1)
#     # return Response({'result':results1})







   
    
    
