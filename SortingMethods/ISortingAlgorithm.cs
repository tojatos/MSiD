namespace SortingMethods
{
    public interface ISortingAlgorithm
    {
        string Name { get; }
        void Sort(ref int[] numbers);
    }
}
