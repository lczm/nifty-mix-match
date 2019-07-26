final List<Profile> demoProfiles = [
  new Profile(
    photos: [
      'assets/testphoto.jpg',
      'assets/test2photo.jpg',
    ],
    name: 'Someone Special',
    bio: 'This is the person you want!',
  ),
  new Profile(
    photos: [
      'assets/test2photo.jpg',
      'assets/testphoto.jpg',
    ],
    name: 'Gross Person',
    bio: 'asdsadsa',
  ),
  new Profile(
    photos: [
      'assets/test2photo.jpg',
      'assets/testphoto.jpg',
    ],
    name: 'Me aaaaa',
    bio: 'asdsadsa',
  ),
];

class Profile {
  final List<String> photos;
  final String name;
  final String bio;

  Profile({
    this.photos,
    this.name,
    this.bio
  });
}