import 'package:flutter/widgets.dart';
import 'package:flutterapp/profiles.dart';

class MatchEngine extends ChangeNotifier {
  final List<FashionMatch> _matches;
  int _currentMatchIndex;
  int _nextMatchIndex;

  MatchEngine({
    List<FashionMatch> matches,
}) : _matches = matches {
    _currentMatchIndex = 0;
    _nextMatchIndex = 1;
  }

  FashionMatch get currentMatch => _matches[_currentMatchIndex];

  FashionMatch get nextMatch => _matches[_nextMatchIndex];

  void cycleMatch() {
    if (currentMatch.decision != Decision.undecided) {
      currentMatch.reset();

      _currentMatchIndex = _nextMatchIndex;
      _nextMatchIndex = _nextMatchIndex < _matches.length - 1 ? _nextMatchIndex + 1 : 0;

      notifyListeners();
    }
  }
}

class FashionMatch extends ChangeNotifier {
  final Profile profile;
  Decision decision = Decision.undecided;

  FashionMatch({
    this.profile
  });

  void one(){
    if (decision == Decision.undecided) {
      decision = Decision.one;
      notifyListeners();
    }
  }

  void two(){
    if (decision == Decision.undecided) {
      decision = Decision.two;
      notifyListeners();
    }
  }

  void three(){
    if (decision == Decision.undecided) {
      decision = Decision.three;
      notifyListeners();
    }
  }

  void four(){
    if (decision == Decision.undecided) {
      decision = Decision.four;
      notifyListeners();
    }
  }

  void five(){
    if (decision == Decision.undecided) {
      decision = Decision.five;
      notifyListeners();
    }
  }

  void reset(){
    if (decision != Decision.undecided) {
      decision = Decision.undecided;
      notifyListeners();
    }
  }
}

enum Decision {
  undecided,
  one,
  two,
  three,
  four,
  five,
}