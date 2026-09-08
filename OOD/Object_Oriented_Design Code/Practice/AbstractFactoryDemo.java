public class AbstractFactoryDemo {
    public static void main(String[] args){
        AbstractFactory shapeFactory = FactoryProducer.getFactory(false);
        Shape shape1= shapeFactory.getShape("Rectangle");
        shape1.draw();
    }
    
}


class FactoryProducer{
    public static AbstractFactory getFactory(boolean rounded){
        if(rounded){
            return new RoundedShapeFactory();
        }
        else{
            return new ShapeFactory();
        }
    }

}


interface Shape{
    void draw();
}

class Rectangle implements Shape{
    public void draw(){
        System.out.println("Rectangle");
    }
}

class RoundedRectangle implements Shape{
    public void draw(){
        System.out.println("Rounded Rectangle");
    }
}

class Square implements Shape{
    public void draw(){
        System.out.println("Square");
    }
}

class RoundedSquare implements Shape{
    public void draw(){
        System.out.println("Rounded Square");
    }
}

abstract class AbstractFactory{
    abstract Shape getShape(String shapeType);
}

class ShapeFactory extends AbstractFactory {
   @Override
   public Shape getShape(String shapeType){    
      if(shapeType.equalsIgnoreCase("RECTANGLE")){
         return new Rectangle();         
      }else if(shapeType.equalsIgnoreCase("SQUARE")){
         return new Square();
      }	 
      return null;
   }
}

class RoundedShapeFactory extends AbstractFactory {
   @Override
   public Shape getShape(String shapeType){    
      if(shapeType.equalsIgnoreCase("RECTANGLE")){
         return new RoundedRectangle();         
      }else if(shapeType.equalsIgnoreCase("SQUARE")){
         return new RoundedSquare();
      }	 
      return null;
   }
}