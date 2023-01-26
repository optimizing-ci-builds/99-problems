name: Java CI
'on':
- push
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: macOS-latest
        java:
        - 8
        - 11
        - 15
      fail-fast: false
      max-parallel: 4
    name: Test JDK ${{ matrix.java }}, ${{ matrix.os }}
    steps:
    - uses: actions/checkout@v1
    - name: Set up JDK
      uses: actions/setup-java@v1
      with:
        java-version: ${{ matrix.java }}
    - name: Test with Maven
      run: mvn test -B --file java8/pom.xml
