from typing import Union, overload, List, Tuple, TypeVar, Text, NewType, Any, Iterable, Optional, Callable, Iterator, \
    Set

# Constants
#=======================================================================================================================
# custom types
_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_S = TypeVar("_S")
Color = NewType("Color", int)  # todo fix the type and everywhere it is used
char = NewType("char", str)
byte = NewType("byte", bytes)
REGEX = NewType("REGEX", str)  # todo fix the type and everywhere it is used

#PI
QUARTER_PI: float = ...
HALF_PI: float = ...
PI: float = ...
TWO_PI: float = ...
TAU: float = ...

# Renderers
P2D: int = ...
P3D: int = ...
PDF: int = ...
SVG: int = ...

# Shapes
ELLIPSE: int = ...
RECT: int = ...
ARC: int = ...
TRIANGLE: int = ...
SPHERE: int = ...
BOX: int = ...
QUAD: int = ...
LINE: int = ...
GROUP: int = ...

# Geometry
POINTS: int = ...
LINES: int = ...
TRIANGLES: int = ...
TRIANGLE_FAN: int = ...
TRIANGLE_STRIP: int = ...
QUADS: int = ...
QUAD_STRIP: int = ...

# Arc Modes
PIE: int = ...
OPEN: int = ...
CHORD: int = ...

# Ellipse Modes
CENTER: int = ...
RADIUS: int = ...
CORNER: int = ...
CORNERS: int = ...

#Texture Modes
IMAGE: int = ...
NORMAL: int = ...

# Mouse
LEFT: int = ...
RIGHT: int = ...
# CENTER: int =... # already implement above in Ellipse Modes
mouseButton: int = ...  #todo: add mouseClicked, mouseDragged,mouseMoved,mousePressed,mouseReleased,mouseWheel
mousePressed: bool = ...
mouseX: int = ...
mouseY: int = ...
pmouseX: int = ...
pmouseY: int = ...

# Keyboard
key: Text = ...  # todo: check type
keyCode: int = ...
keyPressed: bool = ...

# Blend Modes
BLEND: int = ...
ADD: int = ...
SUBTRACT: int = ...
DARKEST: int = ...
LIGHTEST: int = ...
DIFFERENCE: int = ...
EXCLUSION: int = ...
MULTIPLY: int = ...
SCREEN: int = ...
OVERLAY: int = ...
HARD_LIGHT: int = ...
SOFT_LIGHT: int = ...
DODGE: int = ...
BURN: int = ...
REPLACE: int = ...

# Image Modes
# already implemented in Ellipse Modes above
# CORNER: int =...
# CORNERS: int =...
# CENTER: int =...

# Image Filter Modes
THRESHOLD: int = ...
GRAY: int = ...
OPAQUE: int = ...
INVERT: int = ...
POSTERIZE: int = ...
BLUR: int = ...
ERODE: int = ...
DILATE: int = ...

# Texture Wrap Modes
CLAMP: int = ...
REPEAT: int = ...

# Text Modes
MODEL: int = ...
SHAPE: int = ...

# Text Align Modes
TOP: int = ...
# CENTER: int = ... # already defined above in Ellipse Modes
BOTTOM: int = ...
BASELINE: int = ...


class PImage:
    pixels: List[float] = ...
    width: float = ...
    height: float = ...

    def loadPixels(self) -> None: ...

    @overload
    def updatePixels(self) -> None: ...

    @overload
    def updatePixels(self, x: float, y: float, w: float, h: float) -> None: ...

    def resize(self, w: float, h: float) -> None: ...

    @overload
    def get(self) -> List[float]: ...  # todo check return type

    @overload
    def get(self, x: float, y: float) -> List[float]: ...

    @overload
    def get(self, x: float, y: float, w: float, h: float) -> List[float]: ...

    @overload
    def set(self, x: float, y: float, c: Union[Color, int]) -> None: ...

    @overload
    def set(self, x: float, y: float, img: PImage) -> None: ...

    @overload
    def mask(self, maskArray: List) -> None: ...

    @overload
    def mask(self, img: PImage) -> None: ...

    @overload
    def filter(self, kind: int) -> None: ...

    @overload
    def filter(self, kind: int, *params) -> None: ...

    @overload
    def copy(self) -> PImage: ...

    @overload
    def copy(self, sx: float, sy: float, sw: float, sh: float, dx: float, dy: float, dw: float, dh: float) -> Union[
        PImage, None]: ...

    @overload
    def copy(self, src: PImage, sx: float, sy: float, sw: float, sh: float, dx: float, dy: float, dw: float,
             dh: float) -> Union[PImage, None]: ...

    @overload
    def blend(self, sx: float, sy: float, sw: float, sh: float, dx: float, dy: float, dw: float, dh: float,
              mode: int) -> Union[PImage, None]: ...

    @overload
    def blend(self, src: PImage, sx: float, sy: float, sw: float, sh: float, dx: float, dy: float, dw: float, dh: float,
              mode: int) -> Union[PImage, None]: ...

    def save(self, fileName: str) -> None: ...


class PShape:
    width: float = ...
    height: float = ...

    def isVisible(self) -> bool: ...

    def setVisible(self, setVisible: bool) -> None: ...

    def disableStyle(self) -> None: ...

    def enableStyle(self) -> None: ...

    def beginContour(self) -> None: ...

    def endContour(self) -> None: ...

    @overload
    def beginShape(self) -> None: ...

    @overload
    def beginShape(self, kind: int) -> None: ...

    @overload
    def endShape(self) -> None: ...

    @overload
    def endShape(self, kind: int) -> None: ...

    def getChildCount(self) -> None: ...

    @overload
    def addChild(self, who: PShape) -> None: ...

    @overload
    def addChild(self, who: PShape, idx: int) -> None: ...

    @overload
    def getChild(self, index: int) -> PShape: ...

    @overload
    def getChild(self, target: str) -> PShape: ...

    def getVertexCount(self) -> int: ...

    def getVertex(self) -> int: ...

    @overload
    def setVertex(self, index: int, x: float, y: float) -> None: ...

    @overload
    def setVertex(self, index: int, x: float, y: float, z: float) -> None: ...

    @overload
    def setFill(rgb: Union[Color, int]) -> None: ...  # todo fix type

    @overload
    def setFill(self, rgb: Union[Color, int], _alpha: float) -> None: ...

    @overload
    def setFill(self, gray: Union[Color, float]) -> None: ...

    @overload
    def setFill(self, gray: Union[Color, float], _alpha: float) -> None: ...

    @overload
    def setFill(self, v1: float, v2: float, v3: float) -> None: ...

    @overload
    def setFill(self, v1: float, v2: float, v3: float, _alpha: float) -> None: ...

    @overload
    def setStroke(self, rgb: Union[Color, int]) -> None: ...  # todo fix type

    @overload
    def setStroke(self, rgb: Union[Color, int], _alpha: float) -> None: ...

    @overload
    def setStroke(self, gray: Union[Color, float]) -> None: ...

    @overload
    def setStroke(self, gray: Union[Color, float], _alpha: float) -> None: ...

    @overload
    def setStroke(self, v1: float, v2: float, v3: float) -> None: ...

    @overload
    def setStroke(self, v1: float, v2: float, v3: float, _alpha: float) -> None: ...

    @overload
    def translate(self, x: float, y: float) -> None: ...

    @overload
    def translate(self, x: float, y: float, z: float) -> None: ...

    def rotate(self, angle: float) -> None: ...

    def rotateX(self, angle: float) -> None: ...

    def rotateY(self, angle: float) -> None: ...

    def rotateZ(self, angle: float) -> None: ...

    @overload
    def scale(self, s: float) -> None: ...

    @overload
    def scale(self, x: float, y: float) -> None: ...

    @overload
    def scale(self, x: float, y: float, z: float) -> None: ...

    def resetMatrix(self) -> None: ...


class PVector:
    x: float = ...
    y: float = ...

    @overload
    def __init__(self, x: float, y: float): ...

    @overload
    def __init__(self, x: float, y: float, z: float): ...

    @overload
    def set(self, v: PVector) -> None: ...

    @overload
    def set(self, x: float, y: float) -> None: ...

    @overload
    def set(self, x: float, y: float, z: float) -> None: ...

    @overload
    def set(self, source: List[float]) -> None: ...

    @staticmethod
    @overload
    def random2D() -> PVector: ...

    @staticmethod
    @overload
    def random3D() -> PVector: ...

    @staticmethod
    def fromAngle(angle: float) -> PVector: ...

    def copy(self) -> PVector: ...

    def mag(self) -> float: ...

    def magSq(self) -> float: ...

    @overload
    def add(self, v: PVector) -> None: ...

    @overload
    def add(self, x: float, y: float, z: float) -> None: ...

    @staticmethod
    @overload
    def add(v1: PVector, v2: PVector) -> PVector: ...

    @overload
    def sub(self, v: PVector) -> None: ...

    @overload
    def sub(self, x: float, y: float, z: float) -> None: ...

    @staticmethod
    @overload
    def sub(v1: PVector, v2: PVector) -> PVector: ...

    @overload
    def mult(self, n: float) -> None: ...

    @staticmethod
    @overload
    def mult(self, v: PVector, n: float) -> PVector: ...

    @overload
    def div(self, n: float) -> None: ...

    @staticmethod
    @overload
    def div(self, v: PVector, n: float) -> PVector: ...

    @overload
    def dist(self, v: PVector) -> float: ...

    @staticmethod
    @overload
    def dist(self, v1: PVector, v2: PVector) -> float: ...

    @overload
    def dot(self, v: PVector) -> None: ...

    @overload
    def dot(self, x: float, y: float, z: float) -> None: ...

    @staticmethod
    @overload
    def dot(v1: PVector, v2: PVector) -> PVector: ...

    @overload
    def cross(self, v: PVector) -> None: ...

    @staticmethod
    @overload
    def cross(v1: PVector, v2: PVector) -> PVector: ...

    @overload
    def normalize(self) -> None: ...

    def limit(self, _max: float): ...

    @overload
    def setMag(self, _len: float) -> None: ...

    def heading(self) -> float: ...

    def rotate(self, angle) -> None: ...

    @overload
    def lerp(self, v: PVector, amt: float) -> None: ...

    @overload
    def lerp(self, x: float, y: float, z: float, amt: float) -> None: ...

    @staticmethod
    @overload
    def lerp(self, v1: PVector, v2: PVector, amt: float) -> PVector: ...

    @staticmethod
    @overload
    def angleBetween(v1: PVector, v2: PVector) -> float: ...

    def array(self) -> List[float]: ...


class BufferedReader:
    def readLine(self) -> str: ...


class PrintWriter: ...  # todo implement -> was not found


class PGraphics:
    def beginDraw(self) -> None: ...

    def endDraw(self) -> None: ...


class PShader: ...  # todo implement -> was not found


class PFont:
    def list(self) -> List[str]: ...


# Structure
#=======================================================================================================================
def add_library(libraryName: str) -> None: ...


def loop() -> None: ...


def noLoop() -> None: ...


def pushStyle() -> None: ...


def popStyle() -> None: ...


def redraw() -> None: ...


# Environment
#=======================================================================================================================
displayHeight: int = ...
displayWidth: int = ...
focused: bool = ...
frameCount: int = ...
frameRate: int = ...
height: int = ...
width: int = ...


@overload
def cursor(kind: int) -> None: ...


@overload
def cursor(img: PImage) -> None: ...


@overload
def cursor(img: PImage, x: int, y: int) -> None: ...


@overload
def cursor() -> None: ...


def frameRate(fpc: float) -> None: ...


@overload
def fullScreen() -> None: ...


@overload
def fullScreen(screen: int) -> None: ...


@overload
def fullScreen(renderer: int, screen: int) -> None: ...


def noCursor() -> None: ...


@overload
def size(w: int, h: int) -> None: ...


@overload
def size(w: int, h: int, renderer: int) -> None: ...


# Data
#=======================================================================================================================
@overload
def binary(value: Union[char, byte, int]) -> str: ...


@overload
def binary(value: Union[char, byte, int], digits: int) -> str: ...


# def float(i :int) -> float:...

# @overload
# def hex(c: color) -> str:...
# @overload
# def hex(c: color, i: int) -> str:...

# @overload
# def int(value: [float, str]) -> int:...
# @overload
# def int(value: [float, str], base: int) -> int:...

# def list(x: __iterable) -> list:... # TODO: fix data type and methods for it and for dict

# def str(var) -> str:...

def unbinary(_str: str) -> int: ...


def unhex(_str: str) -> int: ...


# String Functions
#=======================================================================================================================

def match(txt: str, regexp: REGEX) -> list: ...


def matchAll(txt: str, regexp: REGEX) -> list: ...  # TODO: check return type


@overload
def nf(num: [int, float], digits: int) -> str: ...


@overload
def nf(num: [int, float], left: int, right: int) -> str: ...


@overload
def nfc(num: [int, float]) -> str: ...


@overload
def nfc(num: [int, float], right: int): ...


@overload
def nfp(num: [int, float], digits: int): ...


@overload
def nfp(num: [int, float], left: int, right: int): ...


@overload
def nfs(num: [int, float], digits: int): ...


@overload
def nfs(num: [int, float], left: int, right: int): ...


# Shape
#=======================================================================================================================
@overload
def createShape() -> PShape: ...


@overload
def createShape(_shape: int, *args) -> PShape: ...


# 2D Primitives
#=======================================================================================================================

@overload
def arc(a: float, b: float, c: float, d: float, start: float, stop: float) -> None: ...


@overload
def arc(a: float, b: float, c: float, d: float, start: float, stop: float, mode: int) -> None: ...


def circle(a: float, b: float, diameter: float) -> None: ...


def ellipse(a: float, b: float, c: float, d: float) -> None: ...


@overload
def line(x1: float, y1: float, x2: float, y2: float) -> None: ...


@overload
def line(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> None: ...


@overload
def point(x: float, y: float) -> None: ...


@overload
def point(x: float, y: float, z: float) -> None: ...


def quad(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> None: ...


@overload
def rect(a: float, b: float, c: float, d: float) -> None: ...


@overload
def rect(a: float, b: float, c: float, d: float, r: float) -> None: ...


@overload
def rect(a: float, b: float, c: float, d: float, tl: float, tr: float, br: float, bl: float) -> None: ...


def square(a: float, b: float, extent: float) -> None: ...


def triangle(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> None: ...


@overload
def bezier(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> None: ...


@overload
def bezier(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float,
           y4: float, z4: float) -> None: ...


def bezierDetail(detail: int) -> None: ...


def bezierPoint(a: float, b: float, c: float, d: float, t: float) -> float: ...


def bezierTangent(a: float, b: float, c: float, d: float, t: float) -> float: ...


@overload
def curve(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> None: ...


@overload
def curve(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float,
          y4: float, z4: float) -> None: ...


def curveDetail(detail: int) -> None: ...


def curvePoint(a: float, b: float, c: float, d: float, t: float) -> float: ...


def curveTangent(a: float, b: float, c: float, d: float, t: float) -> float: ...


def curveTightness(tightness: float) -> None: ...


# 3D Primitives
#=======================================================================================================================

@overload
def box(_size: float) -> None: ...


@overload
def box(w: float, h: float, d: float) -> None: ...


def sphere(r: float) -> None: ...


@overload
def sphereDetail(res: int) -> None: ...


@overload
def sphereDetail(ures: int, vres: int) -> None: ...


# Attributes
#=======================================================================================================================

def ellipseMode(mode: int) -> None: ...


def noSmooth() -> None: ...


def rectMode(mode: int) -> None: ...


@overload
def smooth() -> None: ...


@overload
def smooth(level) -> None: ...


def strokeMode(mode: int) -> None: ...


def strokeJoin(mode: int) -> None: ...


def strokeWeight(weight: float) -> None: ...


# Vertex
#=======================================================================================================================

def beginContour() -> None: ...


def endContour() -> None: ...


def beginShape() -> None: ...


def endShape() -> None: ...


@overload
def bezierVertex(x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> None: ...


@overload
def bezierVertex(x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float,
                 z4: float) -> None: ...


@overload
def curveVertex(x: float, y: float) -> None: ...


@overload
def curveVertex(x: float, y: float, z: float) -> None: ...


@overload
def quadraticVertex(cx: float, cy: float, x3: float, y3: float) -> None: ...


@overload
def quadraticVertex(cx: float, cy: float, cz: float, x3: float, y3: float, z3: float) -> None: ...


def texture(img: PImage) -> None: ...


def textureMode(mode: int) -> None: ...


@overload
def vertex(x: float, y: float) -> None: ...


@overload
def vertex(x: float, y: float, z: float) -> None: ...


@overload
def vertex(x: float, y: float, u: float, v: float) -> None: ...


# Loading & Displaying
#=======================================================================================================================

@overload
def loadShape(filename: str) -> PShape: ...


@overload
def loadShape(filename: str, *options) -> PShape: ...


@overload
def shape(_shape: PShape) -> None: ...


@overload
def shape(_shape: PShape, x: float, y: float) -> None: ...


@overload
def shape(_shape, a: float, b: float, c: float, d: float) -> None: ...


def shapeMode(mode: int) -> None: ...


# Input - Mouse
#=======================================================================================================================


# Input - Keyboard
#=======================================================================================================================


# Input - Files
#=======================================================================================================================

def createReader(filename: str) -> BufferedReader: ...


def loadBytes(filename: str) -> bytearray: ...


@overload
def loadStrings(filename: str) -> list: ...


@overload
def loadStrings(reader: BufferedReader) -> list: ...


def selectFolder(msg: str, callback: str) -> None: ...


def selectInput(msg: str, callback: str) -> None: ...


# Input - Time & Date
#=======================================================================================================================

def day() -> int: ...


def hour() -> int: ...


def millis() -> int: ...


def minute() -> int: ...


def month() -> int: ...


def second() -> int: ...


def year() -> int: ...


# Output - Text Area
#=======================================================================================================================

def println(*args) -> None: ...


# Output - Files
#=======================================================================================================================

def save(filename: str) -> None: ...


@overload
def saveFrame() -> None: ...


@overload
def saveFrame(filename: str) -> None: ...


# Output - Image
#=======================================================================================================================

def beginRaw(renderer: int, filename: str) -> None: ...


def endRaw() -> None: ...


def createWriter(fileName: str) -> PrintWriter: ...


def saveBytes(filename: str, data: List[bytes]) -> None: ...


def saveStrings(filename: str, data: List[str]) -> None: ...


def selectOutput(msg: str, callback: str) -> None: ...


# Transform
#=======================================================================================================================

@overload
def applyMatrix(source) -> None: ...


@overload
def applyMatrix(n00: float, n01: float, n02: float, n10: float, n11: float, n12: float) -> None: ...


@overload
def applyMatrix(n00: float, n01: float, n02: float, n03: float, n10: float, n11: float, n12: float, n13: float,
                n20: float, n21: float, n22: float, n23: float, n30: float, n31: float, n32: float,
                n33: float) -> None: ...


def pushMatrix() -> None: ...


def popMatrix() -> None: ...


def printMatrix() -> None: ...


def resetMatrix() -> None: ...


@overload
def rotate(angle: float) -> None: ...


@overload
def rotate(angle: float, x: float, y: float, z: float) -> None: ...


def rotateX(angle: float) -> None: ...


def rotateY(angle: float) -> None: ...


def rotateZ(angle: float) -> None: ...


@overload
def scale(s: float) -> None: ...


@overload
def scale(x: float, y: float) -> None: ...


@overload
def scale(x: float, y: float, z: float) -> None: ...


def shearX(angle: float) -> None: ...


def shearY(angle: float) -> None: ...


@overload
def translate(x: float, y: float) -> None: ...


@overload
def translate(x: float, y: float, z: float) -> None: ...


@overload
def translate() -> None: ...


# Lights, Camera - Lights
#=======================================================================================================================

@overload
def ambientLight(v1: float, v2: float, v3: float) -> None: ...


@overload
def ambientLight(v1: float, v2: float, v3: float, x: float, y: float, z: float) -> None: ...


def directionalLight(v1: float, v2: float, v3: float, nx: float, ny: float, nz: float) -> None: ...


def lightFalloff(constant: float, linear: float, quadratic: float) -> None: ...


def lightSpecular(v1: float, v2: float, v3: float) -> None: ...


def lights() -> None: ...


def noLights() -> None: ...


def normal(nx: float, ny: float, nz: float) -> None: ...


def pointLight(v1: float, v2: float, v3: float, x: float, y: float, z: float) -> None: ...


def spotLight(v1: float, v2: float, v3: float, x: float, y: float, z: float, nx: float, ny: float, nz: float,
              angle: float, concentration: float) -> None: ...


# Lights, Camera - Camera
#=======================================================================================================================

def beginCamera() -> None: ...


def endCamera() -> None: ...


@overload
def camera() -> None: ...


@overload
def camera(eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float,
           upY: float, upZ: float) -> None: ...


def frustum(left: float, right: float, bottom: float, top: float, near: float, far: float) -> None: ...


@overload
def ortho() -> None: ...


@overload
def ortho(left: float, right: float, bottom: float, top: float) -> None: ...


@overload
def ortho(left: float, right: float, bottom: float, top: float, near: float, far: float) -> None: ...


@overload
def perspective() -> None: ...


@overload
def perspective(fovy: float, aspect: float, zNear: float, zFar: float) -> None: ...


def printCamera() -> None: ...


def printProjection() -> None: ...


# Lights, Camera - Coordinates
#=======================================================================================================================

def modelX(x: float, y: float, z: float) -> float: ...


def modelY(x: float, y: float, z: float) -> float: ...


def modelZ(x: float, y: float, z: float) -> float: ...


@overload
def screenX(x: float, y: float) -> float: ...


@overload
def screenX(x: float, y: float, z: float) -> float: ...


@overload
def screenY(x: float, y: float) -> float: ...


@overload
def screenY(x: float, y: float, z: float) -> float: ...


@overload
def screenZ(x: float, y: float) -> float: ...


@overload
def screenZ(x: float, y: float, z: float) -> float: ...


# Lights, Camera - Material Properties
#=======================================================================================================================

@overload
def ambient(rgb: Union[Color, int]) -> None: ...


@overload
def ambient(gray: Union[Color, float]) -> None: ...


@overload
def ambient(v1: float, v2: float, v3: float) -> None: ...


@overload
def emissive(rgb: Union[Color, int]) -> None: ...


@overload
def emissive(gray: Union[Color, float]) -> None: ...


@overload
def emissive(v1: float, v2: float, v3: float) -> None: ...


@overload
def specular(rgb: Union[Color, int]) -> None: ...


@overload
def specular(gray: Union[Color, float]) -> None: ...


@overload
def specular(v1: float, v2: float, v3: float) -> None: ...


def shininess(shine: float) -> None: ...


# Color - Setting
#=======================================================================================================================

@overload
def background(rgb: Union[Color, int]) -> None: ...


@overload
def background(rgb: Union[Color, int], _alpha: float) -> None: ...


@overload
def background(gray: Union[Color, float]) -> None: ...


@overload
def background(gray: Union[Color, float], _alpha: float) -> None: ...


@overload
def background(v1: float, v2: float, v3: float) -> None: ...


@overload
def background(v1: float, v2: float, v3: float, _alpha: float) -> None: ...


@overload
def background(_image: PImage) -> None: ...


def clear() -> None: ...


@overload
def colorMode(mode: int) -> None: ...


@overload
def colorMode(mode: int, _max: float) -> None: ...


@overload
def colorMode(mode: int, max1: float, max2: float, max3: float) -> None: ...


@overload
def colorMode(mode: int, max1: float, max2: float, max3: float, maxA: float) -> None: ...


@overload
def fill(rgb: Union[Color, int]) -> None: ...


@overload
def fill(rgb: Union[Color, int], _alpha: float) -> None: ...


@overload
def fill(gray: Union[Color, float]) -> None: ...


@overload
def fill(gray: Union[Color, float], _alpha: float) -> None: ...


@overload
def fill(v1: float, v2: float, v3: float) -> None: ...


@overload
def fill(v1: float, v2: float, v3: float, _alpha: float) -> None: ...


def noFill() -> None: ...


def noStroke() -> None: ...


@overload
def stroke(gs: Union[Color, int]) -> None: ...


@overload
def stroke(r: float, g: float, b: float) -> None: ...


# Color - Creating & Reading
#=======================================================================================================================

def alpha(rgb: int) -> None: ...


def blendColor(c1: Union[Color, int], c2: Union[Color, int], MODE: int) -> None: ...


def red(rgb: Union[Color, int]) -> float: ...


def green(rgb: Union[Color, int]) -> float: ...


def blue(rgb: Union[Color, int]) -> float: ...


def brightness(rgb: Union[Color, int]) -> float: ...


def hue(rgb: Union[Color, int]) -> float: ...


def saturation(rgb: Union[Color, int]) -> float: ...


@overload
def color(gray: Union[Color, int]) -> Color: ...


@overload
def color(gray: Union[Color, int], _alpha: float) -> Color: ...


@overload
def color(v1: float, v2: float, v3: float) -> Color: ...


@overload
def color(v1: float, v2: float, v3: float, _alpha: float) -> Color: ...


def lerpColor(c1: Union[Color, int], c2: Union[Color, int], amt: float) -> Color: ...


# Image
#=======================================================================================================================

def createImage(w: int, h: int, _format: int) -> None: ...


# Image - Loading & Displaying
#=======================================================================================================================

@overload
def image(img: PImage, a: float, b: float) -> None: ...


@overload
def image(img: PImage, a: float, b: float, c: float, d: float) -> None: ...


@overload
def tint(rgb: Union[Color, int]) -> None: ...


@overload
def tint(rgb: Union[Color, int], _alpha: float) -> None: ...


@overload
def tint(gray: Union[Color, float]) -> None: ...


@overload
def tint(gray: Union[Color, float], _alpha: float) -> None: ...


@overload
def tint(v1: float, v2: float, v3: float) -> None: ...


@overload
def tint(v1: float, v2: float, v3: float, _alpha: float) -> None: ...


def imageMode(mode: int) -> None: ...


@overload
def loadImage(filename: str) -> PImage: ...


@overload
def loadImage(filename: str, extension: str) -> PImage: ...


@overload
def requestImage(filename: str) -> PImage: ...


@overload
def requestImage(filename: str, extension: str) -> PImage: ...


def noTint() -> None: ...


# Image - Textures
#=======================================================================================================================

def textureWrap(mode: int) -> None: ...


# Image - Pixels
#=======================================================================================================================
pixels: List[int]


@overload
def blend(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, mode: int) -> None: ...


@overload
def blend(src: PImage, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, mode: int) -> None: ...


@overload
def copy(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int) -> None: ...


@overload
def copy(src: PImage, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int) -> None: ...


@overload
def filter(__function: None, __iterable: Iterable[Optional[_T]]) -> Iterator[_T]: ...


@overload
def filter(__function: Callable[[_T], Any], __iterable: Iterable[_T]) -> Iterator[_T]: ...


@overload
def filter(_shader: PShader) -> None: ...


@overload
def filter(kind: int) -> None: ...


@overload
def filter(kind: int, param: float) -> None: ...


@overload
def get() -> PImage: ...


@overload
def get(x: int, y: int) -> PImage: ...


@overload
def get(x: int, y: int, w: int, h: int) -> PImage: ...


def loadPixels() -> None: ...


@overload  # Builtin set
def set(iterable: Iterable[_T] = ...) -> Set: ...


@overload
def set(keys: list) -> set: ...


@overload
def set(x: int, y: int, c: int) -> None: ...


@overload
def set(x: int, y: int, img: PImage) -> None: ...


def updatePixels() -> None: ...


# Image - Rendering
#=======================================================================================================================


def blendMode(mode: int) -> None: ...


def clip(x1: int, y1: int, x2: int, y2: int) -> None: ...


@overload
def createGraphics(w: int, h: int) -> PGraphics: ...


@overload
def createGraphics(w: int, h: int, renderer: int) -> None: ...


@overload
def createGraphics(w: int, h: int, renderer: int, path: str) -> None: ...


def noClip() -> None: ...


# Image - Shaders
#=======================================================================================================================


@overload
def loadShader(fragFilename: str) -> None: ...


@overload
def loadShader(fragFilename: str, vertFilename: str) -> None: ...


@overload
def resetShader() -> None: ...


@overload
def resetShader(kind: int) -> None: ...


@overload
def shader(_shader: PShader) -> None: ...


@overload
def shader(_shader: PShader, kind: int) -> None: ...  # implement constants


# Typography
#=======================================================================================================================


# Typography - Loading & Displaying
#=======================================================================================================================

@overload
def createFont(name: str, _size: float) -> PFont: ...


@overload
def createFont(name: str, _size: float, _smooth: bool) -> PFont: ...


@overload
def createFont(name: str, _size: float, _smooth: bool, charset: list) -> None: ...


def loadFont(filename: str) -> PFont: ...


@overload
def text(txt: str, x: float, y: float) -> None: ...


@overload
def text(txt: str, x: float, y: float, z: float) -> None: ...


@overload
def text(txt: str, x1: float, y1: float, x2: float, y2: float) -> None: ...


@overload
def textFont(font: PFont) -> None: ...


@overload
def textFont(font: PFont, _size: float) -> None: ...


# Typography - Attributes
#=======================================================================================================================

@overload
def textAlign(mode: int) -> None: ...


@overload
def textAlign(modeX: int, modeY: int) -> None: ...


def textLeading(spacing: int) -> None: ...


def textMode(mode: int) -> None: ...


def testSize(size: int) -> None: ...


def textWidth(txt: str) -> None: ...


# Typography - Attributes
#=======================================================================================================================

def textAscent() -> float: ...


def textDescent() -> float: ...


# Math - Calculation
#=======================================================================================================================

# def abs(n: float) -> float:...

def ceil(n: float) -> int: ...


def constrain(amt: float, low: float, high: float) -> float: ...


@overload
def dist(x1: float, y1: float, x2: float, y2: float) -> float: ...


@overload
def dist(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float: ...


def exp(n: float) -> float: ...


def floor(n: float) -> int: ...


def lerp(start: float, stop: float, amt: float) -> float: ...


def log(n: float) -> float: ...


def mag(x: float, y: float) -> float: ...


@overload  # Builtin function
def map(__func: Callable[[_T1], _S], __iter1: Iterable[_T1]) -> Iterator[_S]: ...


@overload
def map(func, list) -> list: ...


@overload
def map(value: float, start1: float, stop1: float, start2: float, stop2: float) -> float: ...


# @overload
# def max(a: float, b: float, *args) -> float:...
# @overload
# def max(List[int]) -> float:...

# @overload
# def min(a: float, b: float, *args) -> float:...
# @overload
# def min(List[int]) -> float:...

def norm(value: float, start: float, stop: float) -> float: ...


# def pow(n: float, e: float) -> float:...

# def round(n: float) -> int:...

def sq(n: float) -> float: ...


# def sqrt(n: float) -> float:...

# Math - Trigonometry
#=======================================================================================================================

def sin(value: float) -> float: ...


def cos(value: float) -> float: ...


def tan(value: float) -> float: ...


def asin(value: float) -> float: ...


def acos(value: float) -> float: ...


def atan(value: float) -> float: ...


def atan2(y: float, x: float) -> float: ...


def degrees(value: float) -> float: ...


def radians(value: float) -> float: ...


# Math - Random
#=======================================================================================================================

@overload
def noise(x: float) -> float: ...


@overload
def noise(x: float, y: float) -> float: ...


@overload
def noise(x: float, y: float, z: float) -> float: ...


@overload
def noiseDetail(lod: int) -> None: ...


@overload
def noiseDetail(lod: int, falloff: float) -> None: ...


def noiseSeed(seed: int) -> None: ...


@overload
def random(high: float) -> float: ...


@overload
def random(low: float, high: float) -> float: ...


def randomGaussian() -> float: ...


def randomSeed(seed: int) -> None: ...
